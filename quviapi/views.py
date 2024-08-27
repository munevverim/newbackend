from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import requests
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import string
from concurrent.futures import ThreadPoolExecutor
import io
import base64
from PIL import Image
from googletrans import Translator, LANGUAGES
from io import BytesIO
from rembg import remove
import requests
from django.contrib.auth.decorators import login_required
from .models import CustomUser
import os

def index(request):
    return render(request, "index.html")

@csrf_protect
@login_required
def projectChoose(request):
    if not request.user.is_authenticated or not request.user.id:
        return JsonResponse({"error": "Unauthorized access."}, status=401)

    try:
        custom_user = CustomUser.objects.get(id=request.user.id)
    except CustomUser.DoesNotExist:
        return JsonResponse({"error": "User does not exist."}, status=404)
    user = CustomUser.objects.get(id=request.user.id)
    context = {'user': user}
    return render(request, "project.html", context)

@csrf_protect
@login_required
def userInfo(request):
    if not request.user.is_authenticated or not request.user.id:
        return JsonResponse({"error": "Unauthorized access."}, status=401)

    try:
        json_data = json.loads(request.body)
        c_value = json_data.get("v")
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format in request body."}, status=400)
    
    try:
        custom_user = CustomUser.objects.get(id=request.user.id)
    except CustomUser.DoesNotExist:
        return JsonResponse({"error": "User does not exist."}, status=404)
    
    c_front_value = None
    t_front_value = None

    if c_value == "1":
        c_front_value = custom_user.c1
        t_front_value = custom_user.t1
    elif c_value == "2":
        c_front_value = custom_user.c2
        t_front_value = custom_user.t2
    elif c_value == "3":
        c_front_value = custom_user.c3
        t_front_value = custom_user.t3
    elif c_value == "4":
        c_front_value = custom_user.c4
        t_front_value = custom_user.t4
    elif c_value == "5":
        c_front_value = custom_user.c5
        t_front_value = custom_user.t5
    else:
        return JsonResponse({"error": "Invalid c value."}, status=400)

    return JsonResponse({'c': c_front_value, 't': t_front_value})

@csrf_protect
@login_required
def editor(request):
    if not request.user.is_authenticated or not request.user.id:
        return JsonResponse({"error": "Unauthorized access."}, status=401)

    # Kullanıcının kredi kontrolü ve azaltma işlemi
    try:
        custom_user = CustomUser.objects.get(id=request.user.id)
    except CustomUser.DoesNotExist:
        return JsonResponse({"error": "User does not exist."}, status=404)
    user = CustomUser.objects.get(id=request.user.id)
    context = {'user': user}
    return render(request, "editor.html", context)

@csrf_protect
def generate_canvas(request):
    image_list = []

    # Kullanıcının Google ile giriş yapmış olduğunu ve id'sinin mevcut olduğunu kontrol ediyoruz
    if not request.user.is_authenticated or not request.user.id:
        return JsonResponse({"error": "Unauthorized access."}, status=401)

    # Kullanıcının kredi kontrolü ve azaltma işlemi
    try:
        custom_user = CustomUser.objects.get(id=request.user.id)
    except CustomUser.DoesNotExist:
        return JsonResponse({"error": "User does not exist."}, status=404)
    
    if custom_user.credit < 5:  # Kullanıcı işlem yapmak için yeterli krediye sahip değilse
        return JsonResponse({"error": "Insufficient credit."}, status=400)

    # Kredi azaltma işlemi
    custom_user.credit -= 5
    custom_user.save()

    with open('quviapi/blacklist.txt', 'r', encoding='utf-8') as file:
        blacklist = set(line.strip().lower() for line in file)

    json_data = json.loads(request.body)
    prompt_value = json_data.get("prompt")
    prompt_value = translate(prompt_value)

    punctuations = string.punctuation
    for char in punctuations:
        prompt_value = prompt_value.replace(char, f" {char} ")

    snp = "nsfw, bad anatomy, bad proportions, blurry, cloned face, cropped, deformed, dehydrated, disfigured, duplicate, error, extra arms, extra legs, extra limbs, fused fingers, gross proportons, jpeg artifacts, long neck, low quality, lowres, malformed limbs, missing arms, missing legs, morbid, mutated hands, mutation, mutilated, out of frame, poorly drawn face,poorly drawn hands, signature, text, too many fingers, ugly, username, watermark, worst quality, "+"nsfw, "+"nude, "+"sex, "+"anal, "+"sexuality, "+"porn, "+"dick, "+"cock, "+"vagina, "+"tit, "+"tits, "+"boobs, "+"cunt, "+"blowjob, "+"handjob, "+"pornography, "+"ass, "+"gay, "+"pee, "+"bad pixels, "+"lowres, "+"medium resolution, "+"low resolution, "+"deformation, "+"blurry, "+"deformed, "+"cropped, "+"low quality, "+"text, "+"worst quality, "+"username, "+"out of frame, "+"jpeg artifacts, "+"duplicate, "+"disfigured, "+"error, "+"bad illustration, "+"di512rted, "+"fault, "+"hazy, "+"flaw, "+"logo, "+"incorrect ratio, "+"mistake, "+"pixelated, "+"script, "+"sign, "+"tiling, "+"distorted details, "+"opaque, "+"underexposed, "+"surreal, "+"distortion, "+"text, "

    prompt_words = [word.strip().lower() for word in prompt_value.split() if word.strip().lower() not in blacklist]
    prompt_value = ' '.join(prompt_words)

    imageInCanvas = json_data.get("image")

    imageInCanvas = imageInCanvas[22:]
    
    styleDraw = json_data.get("style")
    weather = json_data.get("weather")
    
    scale_value = json_data.get("scale")
    if scale_value == 's':
        scale_value = 1
    elif scale_value == 'h':
        scale_value = 2
    elif scale_value == 'v':
        scale_value = 3
        
    if scale_value == 1:
        height = 768
        width = 768
    elif scale_value == 2:
        height = 576
        width = 768
    elif scale_value == 3:
        height = 768
        width = 576

    inorex = json_data.get("design")

    if inorex =='Interior':
        styles = ["sai-photographic", styleDraw, inorex, weather ]
    elif inorex == 'Exterior':
        styles = ["sai-photographic", styleDraw, inorex, weather ]
    elif inorex == 'floor-plan':
        styles = ["sai-photographic", "floorplan"]
    elif inorex == 'landscape':
        styles = ["sai-photographic", "landscape" ]

    buffer = io.BytesIO()
    imgdata = base64.b64decode(imageInCanvas)
    img = Image.open(io.BytesIO(imgdata))
    img = img.resize((width, height))
    img.save(buffer, format="PNG")
    imageInCanvas = base64.b64encode(buffer.getvalue()).decode("utf-8")

    mask = json_data.get("mask")
    if mask == 0:
        mask = mask
    else:
        mask = mask[22:]
        buffer2 = io.BytesIO()
        maskdata = base64.b64decode(mask)
        img2 = Image.open(io.BytesIO(maskdata))
        img2 = img2.resize((width, height))
        img2.save(buffer2, format="PNG")
        mask = base64.b64encode(buffer2.getvalue()).decode("utf-8")


    def api_request(url, payload):
        response = requests.post(url, json=payload)
        return response.json()
    with ThreadPoolExecutor() as executor:
        if mask != 0:
            payload = {
                "prompt": prompt_value,
                "negative_prompt": snp,
                "seed": -1,
                "subseed": -1,
                "cfg_scale": 1,
                "mask_blur": 4,
                "mask_blur_x": 4,
                "mask_blur_y": 4,
                "mask_transparancy": 0,
                "height": height,
                "width": width,
                "sampler_name":"DPM++ SDE Karras",
                "image_cfg_scale":1,
                "resize_mode": 0,
                "resize_by": 1,
                "init_images": [imageInCanvas],
                "steps": 4,
                "denoising_strength": 1,
                "batch_size": 4,
                "mask": mask,
                "mask_mode": 0,
                "inpainting_fill": 1,
                "inpaint_full_res": True,
                "inpaint_full_res_padding": 32,
                "include_init_images": True,
                "alwayson_scripts": {
                    "controlnet": {
                        "args": [
                            {
                                "enabled": True,
                                "module": "canny",
                                "model": "diffusers_xl_canny_full [2b69fca4]",
                                "weight": 0.75,
                                "resize_mode": 0,
                                "image": imageInCanvas,
                                "lowvram": False,
                                "threshold_a": 0,
                                "threshold_b": 255,
                                "guidance_start": 0.0,
                                "guidance_end": 1.0,
                                "control_mode": 1,
                                "pixel_perfect": True
                            }
                        ]
                    }
                }
            }
        else:
            payload = {
                "prompt": prompt_value,
                "negative_prompt": snp,
                "seed": -1,
                "cfg_scale": 2,
                "image_cfg_scale": 35,
                "height": height,
                "width": width,
                "init_images": [imageInCanvas],
                "steps": 4,
                "denoising_strength": 1,
                "styles": styles,
                "batch_size": 4,
                "sampler_name":"DPM++ SDE Karras",
                "alwayson_scripts": {
                    "controlnet": {
                        "args": [
                            {
                                "enabled": True,
                                "module": "canny",
                                "model": "diffusers_xl_canny_full [2b69fca4]",
                                "weight": 1,
                                "image": imageInCanvas,
                                "resize_mode": 0,
                                "lowvram": False,
                                "threshold_a": 0,
                                "threshold_b": 255,
                                "guidance_start": 0.0,
                                "guidance_end": 1.0,
                                "control_mode": 1,
                                "pixel_perfect": True
                            }
                        ]
                    }
                }
            }
        response_future = executor.submit(api_request, f'http://192.168.1.143:7861/sdapi/v1/img2img', payload)

    r = response_future.result()
    
    for idx,i in enumerate(r['images']):
        img = (i.split(",", 1)[0])
        image_list.append(img)

    return JsonResponse({"image": image_list, "credit": custom_user.credit})

@csrf_protect
def generate_index(request):
    image_list = []

    # Kullanıcının Google ile giriş yapmış olduğunu ve id'sinin mevcut olduğunu kontrol ediyoruz
    if not request.user.is_authenticated or not request.user.id:
        return JsonResponse({"error": "Unauthorized access."}, status=401)

    # Kullanıcının kredi kontrolü ve azaltma işlemi
    try:
        custom_user = CustomUser.objects.get(id=request.user.id)
    except CustomUser.DoesNotExist:
        return JsonResponse({"error": "User does not exist."}, status=404)
    
    if custom_user.credit < 5:  # Kullanıcı işlem yapmak için yeterli krediye sahip değilse
        return JsonResponse({"error": "Insufficient credit."}, status=400)

    # Kredi azaltma işlemi
    custom_user.credit -= 5
    custom_user.save()

    with open('quviapi/blacklist.txt', 'r', encoding='utf-8') as file:
        blacklist = set(line.strip().lower() for line in file)

    json_data = json.loads(request.body)
    prompt_value = json_data.get("prompt")
    prompt_value = translate(prompt_value)

    punctuations = string.punctuation
    for char in punctuations:
        prompt_value = prompt_value.replace(char, f" {char} ")

    prompt_words = [word.strip().lower() for word in prompt_value.split() if word.strip().lower() not in blacklist]
    prompt_value = ' '.join(prompt_words)

    inorex = json_data.get("design")
    styleDraw = json_data.get("style")
    scale_value = json_data.get("scale")
    if scale_value == 's':
        scale_value = 1
    elif scale_value == 'h':
        scale_value = 2
    elif scale_value == 'v':
        scale_value = 3
    weather = json_data.get("weather")

    if inorex =='Interior':
        prompt_value = "interior design "+prompt_value+" in the style of "+styleDraw+"."
        styles = ["sai-photographic", styleDraw, inorex, weather ]
    elif inorex == 'Exterior':
        prompt_value = "exterior design "+prompt_value+" in the style of "+styleDraw+"."
        styles = ["sai-photographic", styleDraw, inorex, weather ]
    elif inorex == 'floor-plan':
        prompt_value = "floor plan, perspective, "+prompt_value+"."
        styles = ["sai-photographic", "floorplan"]
    elif inorex == 'landscape':
        prompt_value = "situation plan of "+prompt_value+". aerial photo"
        styles = ["sai-photographic", "landscape" ]

    if scale_value == 1:
        height = 768
        width = 768
    elif scale_value == 2:
        height = 576
        width = 768
    elif scale_value == 3:
        height = 768
        width = 576

    def api_request(url, payload):
        response = requests.post(url, json=payload)
        return response.json()
    
    with ThreadPoolExecutor() as executor:
        payload = {
            "prompt": prompt_value,
            "negative_prompt": "nsfw, close up, partial, part, zoom, ",
            "cfg_scale": 2,
            "steps": 4,
            "width": width,
            "height": height,
            "batch_size": 4,
            "styles": styles,
            "sampler_name":"DPM++ SDE Karras",
        }
        response_future = executor.submit(api_request, f'http://192.168.1.143:7861/sdapi/v1/txt2img', payload)

    r = response_future.result()
    
    for idx,i in enumerate(r['images']):
        img = (i.split(",", 1)[0])
        image_list.append(img)

    return JsonResponse({"image": image_list, "credit": custom_user.credit})

@csrf_protect
def generate_item(request):
    image_list = []

    # Kullanıcının Google ile giriş yapmış olduğunu ve id'sinin mevcut olduğunu kontrol ediyoruz
    if not request.user.is_authenticated or not request.user.id:
        return JsonResponse({"error": "Unauthorized access."}, status=401)

    # Kullanıcının kredi kontrolü ve azaltma işlemi
    try:
        custom_user = CustomUser.objects.get(id=request.user.id)
    except CustomUser.DoesNotExist:
        return JsonResponse({"error": "User does not exist."}, status=404)
    
    if custom_user.credit < 5:  # Kullanıcı işlem yapmak için yeterli krediye sahip değilse
        return JsonResponse({"error": "Insufficient credit."}, status=400)

    # Kredi azaltma işlemi
    custom_user.credit -= 5
    custom_user.save()

    with open('quviapi/blacklist.txt', 'r', encoding='utf-8') as file:
        blacklist = set(line.strip().lower() for line in file)

    json_data = json.loads(request.body)
    prompt_value = json_data.get("prompt")
    prompt_value = translate(prompt_value)

    snp = "nsfw, bad anatomy, bad proportions, blurry, cloned face, cropped, deformed, dehydrated, disfigured, duplicate, error, extra arms, extra legs, extra limbs, fused fingers, gross proportons, jpeg artifacts, long neck, low quality, lowres, malformed limbs, missing arms, missing legs, morbid, mutated hands, mutation, mutilated, out of frame, poorly drawn face,poorly drawn hands, signature, text, too many fingers, ugly, username, watermark, worst quality, "+"nsfw, "+"nude, "+"sex, "+"anal, "+"sexuality, "+"porn, "+"dick, "+"cock, "+"vagina, "+"tit, "+"tits, "+"boobs, "+"cunt, "+"blowjob, "+"handjob, "+"pornography, "+"ass, "+"gay, "+"pee, "+"bad pixels, "+"lowres, "+"medium resolution, "+"low resolution, "+"deformation, "+"blurry, "+"deformed, "+"cropped, "+"low quality, "+"text, "+"worst quality, "+"username, "+"out of frame, "+"jpeg artifacts, "+"duplicate, "+"disfigured, "+"error, "+"bad illustration, "+"di512rted, "+"fault, "+"hazy, "+"flaw, "+"logo, "+"incorrect ratio, "+"mistake, "+"pixelated, "+"script, "+"sign, "+"tiling, "+"distorted details, "+"opaque, "+"underexposed, "+"surreal, "+"distortion, "+"text, "


    punctuations = string.punctuation
    for char in punctuations:
        prompt_value = prompt_value.replace(char, f" {char} ")

    prompt_words = [word.strip().lower() for word in prompt_value.split() if word.strip().lower() not in blacklist]
    prompt_value = ' '.join(prompt_words)

    styleDraw = json_data.get("style")
    scale_value = json_data.get("scale")
    if scale_value == 's':
        scale_value = 1
    elif scale_value == 'h':
        scale_value = 2
    elif scale_value == 'v':
        scale_value = 3

    if prompt_value=='':
        prompt_value = 'furniture'

    prompt_value = prompt_value+" with white background."

    if scale_value == 1:
        height = 512
        width = 512
    elif scale_value == 2:
        height = 384
        width = 512
    elif scale_value == 3:
        height = 512
        width = 384

    def api_request(url, payload):
        response = requests.post(url, json=payload)
        return response.json()
    
    with ThreadPoolExecutor() as executor:
        payload = {
            "prompt": prompt_value,
            "negative_prompt": "nsfw, close up, partial, part, zoom, " + snp,
            "cfg_scale": 1,
            "steps": 4,
            "width": 768,
            "height": 768,
            "batch_size": 4,
            "styles": [],
            "sampler_name":"DPM++ SDE Karras",
            "alwayson_scripts": {
                "LayerDiffuse": {
                    "args": [
                        {
                        "enabled": True,
                        "model": "DPM++ SDE Karras",
                        "weight": 1,
                        "stop_at": 1
                        }
                    ]
                }
            }
        }
        response_future = executor.submit(api_request, f'http://192.168.1.143:7862/sdapi/v1/txt2img', payload)

    r = response_future.result()
    
    for idx,i in enumerate(r['images']):
        img = (i.split(",", 1)[0])
        image_list.append(img)

    return JsonResponse({"image": image_list, "credit": custom_user.credit})

@csrf_protect
def background_cleaner(request):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            image = json_data.get("image")
            image = image[22:]
            decoded_image = base64.b64decode(image)
            image = Image.open(BytesIO(decoded_image))

            output = remove(image)
            
            buffer = BytesIO()
            output.save(buffer, format="PNG")
            output_bytes = buffer.getvalue()

            encoded_image_str = base64.b64encode(output_bytes).decode('utf-8')

            return JsonResponse({"image": encoded_image_str})

        except Exception as e:
            return JsonResponse({"error": f"Image processing failed: {str(e)}"})

    return JsonResponse({"error": "Invalid request method"})


def translate(text):
    if text:
        translator = Translator()

        try:
            detected_language = translator.detect(text)

            if detected_language is not None and detected_language.lang in LANGUAGES:
                detected_language = detected_language.lang
                translated_text = translator.translate(text, src=detected_language, dest='en')

                if translated_text is not None:
                    return translated_text.text
                else:
                    return "Failed to translate"
        except Exception as e:
            return text
    else:
        return ""

@csrf_protect
@login_required
def save_canvas_data(request):
    try:
        if not request.user.is_authenticated or not request.user.id:
            return JsonResponse({"error": "Unauthorized access."}, status=401)

        custom_user = CustomUser.objects.get(username=request.user.username)

        if request.method == 'POST':
            json_data = json.loads(request.body)
            canvas_json_data = json_data.get('canvas_json_data')
            cclear = json_data.get('valueC')
            layers = json_data.get('layerDataFront')
            canvasImage = json_data.get('backendUrl')

            if cclear == "1":
                custom_user.c1 = canvas_json_data
                custom_user.t1 = layers
                custom_user.ci1 = canvasImage
            elif cclear == "2":
                custom_user.c2 = canvas_json_data
                custom_user.t2 = layers
                custom_user.ci2 = canvasImage
            elif cclear == "3":
                custom_user.c3 = canvas_json_data
                custom_user.t3 = layers
                custom_user.ci3 = canvasImage
            elif cclear == "4":
                custom_user.c4 = canvas_json_data
                custom_user.t4 = layers
                custom_user.ci4 = canvasImage
            elif cclear == "5":
                custom_user.c5 = canvas_json_data
                custom_user.t5 = layers
                custom_user.ci5 = canvasImage
            
            custom_user.save()
            return JsonResponse({"message": "Data saved successfully"})
        else:
            return JsonResponse({"error": "Only POST requests are allowed."}, status=405)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
