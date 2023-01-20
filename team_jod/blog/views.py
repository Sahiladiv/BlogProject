from django.shortcuts import render, redirect
from .models import Blogs, Comments

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from . import recommendation, categorization, sentiment_analysis
from transformers import T5Tokenizer, T5Config, T5ForConditionalGeneration, AutoTokenizer 
import pyttsx3
from gingerit.gingerit import GingerIt


import json

#global
# title = ""
# content = ""
# summary = ""




# Create your views here.
def home(request):


    all_blogs = Blogs.objects.all()
    print(all_blogs)
    # result = categorization.main()
    # print(result)


    return render(request, 'blogs.html')

def people_blog(request, q):
    all_blogs = Blogs.objects.all()
    q = q.upper()
    blog_posts = []
    for i in all_blogs:
        if q == i.blog_category: 
            blog_posts.append(i)
    
    return render(request, 'people_blogs.html', {'blog_posts': blog_posts})









def show_blog(request):

    id = request.GET.get('id')
    blog = Blogs.objects.get(id = id)

    recommender_list = recommendation.recommend(blog.blog_title)

    return render(request, 'blog_content.html', {'blog': blog, 'recommender_list':recommender_list})


from django.http import JsonResponse

# def is_ajax(request):
#     return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


#     if is_ajax(request = request):
#         d = request.GET.get('data_content')
#         print(d)
#         return JsonResponse({'data':'hello there'}, status=200)
#     return render(request, 'write_blogs.html')
def write_blog(request):



    if request.user.is_authenticated:
    

        if request.method == 'POST':
                # global title
                # global text_content
                title = request.POST.get('title')
                text_content = request.POST.get('text_content')
                text_content = check_grammar(text_content)
                summary = summarization(text_content)
                category = categorization.categorize_blog(text_content)
                return render(request, 'publish_blog.html', {'title':title,'text_content':text_content,'summary':summary, 'category':category})

        else:

            return render(request, 'write_blogs.html')
    else:
        return redirect ('/accounts/signin')




tokenizer = AutoTokenizer.from_pretrained("Vamsi/T5_Paraphrase_Paws")
model = AutoModelForSeq2SeqLM.from_pretrained("Vamsi/T5_Paraphrase_Paws")

def my_paraphrase(sentence):

    sentence= "paraphrase: "+ sentence + "</s>"
    encoding = tokenizer.encode_plus(sentence,padding=True, return_tensors="pt")
    input_ids, attention_masks=encoding["input_ids"], encoding["attention_mask"]
    
    outputs=model.generate(
        input_ids=input_ids, attention_mask = attention_masks,
        max_length=256,
        do_sample=True,
        top_k=120,
        top_p=0.95,
        early_stopping=True,
        num_return_sequences=1)
    output=tokenizer.decode(outputs[0],skip_special_tokens=True, clean_up_tokenization_spaces=True)
    return(output)


def paraphrase(request):
    
    if request.method == 'POST':
        input_text = request.POST.get('original_text')

        output=" ".join([my_paraphrase(sent) for sent in sent_tokenize(input_text)])
        return render(request, 'paraphrase.html',{'output':output, 'input': input_text})

    return render(request, 'paraphrase.html')


def summarization(data_sent):
    model = T5ForConditionalGeneration.from_pretrained("t5-base")
    tokenizer = AutoTokenizer.from_pretrained("t5-base")
    inputs = tokenizer.encode("summarize: " + data_sent, return_tensors="pt", truncation=True)
    outputs = model.generate(
        inputs, 
        max_length=10000, 
        min_length=40, 
        length_penalty=2.0, 
        num_beams=4, 
        early_stopping=True
    )


    final= tokenizer.decode(outputs[0], skip_special_tokens=True)
    final=final.title()  #captilizes the string
    return final


def publish(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text_content = request.POST.get('text_content')
        text_summary = request.POST.get('text_summary')
        category = request.POST.get('category')

        blog_title = title
        blog_category = category.upper()
        blog_content = text_content
        blog_summary = text_summary

        new_blog = Blogs.objects.create(
            blog_title = blog_title,
            blog_category = blog_category,
            blog_content = blog_content,
            blog_summary = blog_summary
        )
                                                    
        new_blog.save()

        return redirect('/')
        


def check_grammar(data):

    parser = GingerIt()
    ct = parser.parse(data)
    check_data = ct['result']
    print("DATA",check_data)

    return check_data


def demo(request):

    d = request.GET.get('data')
    print(d)
    
import time
 
 

def comment(request):

    all_comments = Comments.objects.all()

    blog_id = str(request.GET.get('id'))
    comment_list = []
    for i in all_comments:
        if str(i.blog_id)== blog_id:
            comment_list.append(i)

    
    


    if(request.method == "POST"):
        comment = request.POST.get('comment')
        comment_type = sentiment_analysis.sentiment(comment)
        timestamp = time.time()
        comment_author = str(request.user)

        new_comment = Comments.objects.create(
            blog_id = blog_id,
            # timestamp = timestamp,
            comment_author = comment_author,
            comment = comment,
            comment_type = comment_type,
        )

        new_comment.save()
        return_statment = '/blogs/comment?id=' + blog_id
        return redirect(return_statment)
    
    return render(request, 'comments.html', {'comment_list':comment_list})