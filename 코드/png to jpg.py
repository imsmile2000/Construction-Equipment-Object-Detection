from PIL import Image

def imgConvert(page_url,save_url):

    im = Image.open(page_url)

    im = im.convert("RGB")
    save_url_change = save_url.replace("png","jpg")
    im.save(save_url_change)
    
#함수실행 
if __name__ == "__main__":

    #변환된 파일이 저장될 폴더(jpg)
    save_url='/content/drive/MyDrive/GRADING_Study/jpgIMG/'
    #변환할 파일이 저장된 폴더(png)
    load_url='/content/drive/MyDrive/GRADING_Study/pngTojpgIMG/'


    os.chdir(load_url)
    images=glob.glob('./*.png')

    images.sort()
       
    for i in range(len(images)):
        filename=images[i]
            
        save_path = save_url+images[i]
        load_path = load_url+images[i]

        imgConvert(load_path,save_path)