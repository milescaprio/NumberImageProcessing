from PIL import Image
def cropToSquare(tocrop):
    '''
    :param Image tocrop: The PIL Image to crop.
    '''
    if tocrop.width % 2:
        print("Odd pixel width. Cutting end column.");
        tocrop = tocrop.crop((0, 0, tocrop.width - 1, tocrop.height));
    if tocrop.height % 2:
        print("Odd pixel height. Cutting end row.");
        tocrop = tocrop.crop((0, 0, tocrop.width, tocrop.height - 1));

    if tocrop.width == tocrop.height:
        return tocrop;
    cropsquare = min(tocrop.size);
        
    if tocrop.width > tocrop.height:
        cropped = tocrop.crop( ( (tocrop.width-cropsquare)/2 , 0 , (tocrop.width+cropsquare)/2, tocrop.height) );
    if tocrop.width < tocrop.height:
        cropped = tocrop.crop( ( 0 , (tocrop.height-cropsquare)/2 , tocrop.width , (tocrop.height+cropsquare)/2) );
    return cropped;
