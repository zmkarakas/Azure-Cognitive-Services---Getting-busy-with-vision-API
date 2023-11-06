# Azure-Cognitive-Services---Getting-busy-with-vision-API

This repo showcases a simple yet powerful api of Azure. To run the code, set up a python virtual env and run the index.py, put a sample photo in the folder together with config.json and run it against your own azure api. I haven't included my own photo that I tested it with. Click below to deploy Computer vision api in your azure subscription. Also, do put your endpoint and your keys for secure connection to api. You can find the keys under Resource Management in the UI. 

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fzmkarakas%2FAzure-Cognitive-Services---Getting-busy-with-vision-API%2Fmain%2Ftemplate.json)

# Describe and Analyze image with tags

I have uploaded myself with glasses in middle of a forest, to see if the api will detect my glasses. It did but confidence values have been lower than my expectation. I have run this test to see if its viable to use it for a startup idea I have. 


The resulting JSON that came from the API looks like this when formatted, which I think is a very good description of the photo "a man wearing glasses":

```
{
   "description":{
      "tags":[
         "tree",
         "person",
         "outdoor",
         "grass",
         "posing"
      ],
      "captions":[
         {
            "text":"a man wearing glasses",
            "confidence":0.517833411693573
         }
      ]
   },
   "requestId":"3eb0f0ec-aab9-4ca3-8ae0-39e625d4030d",
   "metadata":{
      "height":950,
      "width":960,
      "format":"Jpeg"
   },
   "modelVersion":"2021-05-01"
}{
   "tags":[
      {
         "name":"person",
         "confidence":0.9959856271743774
      },
      {
         "name":"human face",
         "confidence":0.9958528876304626
      },
      {
         "name":"clothing",
         "confidence":0.990203320980072
      },
      {
         "name":"tree",
         "confidence":0.9869425296783447
      },
      {
         "name":"outdoor",
         "confidence":0.9435588717460632
      },
      {
         "name":"eyewear",
         "confidence":0.849549412727356
      },
      {
         "name":"shirt",
         "confidence":0.8464416265487671
      },
      {
         "name":"wearing",
         "confidence":0.8161780834197998
      },
      {
         "name":"grass",
         "confidence":0.7622987627983093
      },
      {
         "name":"forest",
         "confidence":0.6811438798904419
      },
      {
         "name":"glasses",
         "confidence":0.6106087565422058
      },
      {
         "name":"red",
         "confidence":0.5914949178695679
      }
   ],
   "requestId":"0eadab26-63dd-478a-8957-90b9870fbc28",
   "metadata":{
      "height":950,
      "width":960,
      "format":"Jpeg"
   },
   "modelVersion":"2021-05-01"
}
```
