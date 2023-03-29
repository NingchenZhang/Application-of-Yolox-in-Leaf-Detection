import os
from lxml import etree, objectify

save_target_path = "newTarget/Annotations"

if not os.path.exists(save_target_path):
    os.makedirs(save_target_path)


def save_2xml(boxes, classes, img, image):
    name = os.path.basename(img)

    save_path = os.path.join(save_target_path, name)
    #print(save_path)
    save_path, _ = save_path.split('.')
    save_path = save_path + '.xml'
    E = objectify.ElementMaker(annotate=False)
    anno_tree = E.annotation(
        E.folder('VOC2007'),
        E.filename(name),
        E.source(
            E.database('The VOC2007 Database'),
            E.annotation('PASCAL VOC2007'),
            E.image('flickr'),
            E.flickrid("325991873")
        ),
        E.size(
            E.width(str(image.width)),
            E.height(str(image.height)),
            E.depth(3)
        ),
        E.segmented(0),
    )
    # print(save_path)
    #print(boxes)
    for box in boxes:
        #print(box)
        top, left, bottom, right = box
        E2 = objectify.ElementMaker(annotate=False)
        anno_tree2 = E2.object(
            E.name('leaf'),
            E.bndbox(
                E.xmin(int(left)),
                E.ymin(int(top)),
                E.xmax(int(right)),
                E.ymax(int(bottom))
            ),
        )
        anno_tree.append(anno_tree2)
    etree.ElementTree(anno_tree).write(save_path, pretty_print=True)