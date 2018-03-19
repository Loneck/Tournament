from sorl.thumbnail import get_thumbnail


def thumbnail(image, widthxheight, crop='center', quality=95):
    im = get_thumbnail(image, widthxheight, crop=crop)
    return im
