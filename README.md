In this project, you built a **Generative AI-powered recipe creation application** using **Amazon Bedrock**. 

Here's a breakdown of what you've accomplished:

1. **Amazon Bedrock Introduction and AWS Configuration**  
   - Explored the **Bedrock Dashboard**  
   - Configured necessary **AWS services** like **S3** and **SageMaker**  

2. **AI Model Selection and Evaluation**  
   - Chose the **Titan Text model** for recipe generation  
   - Reviewed the model’s capabilities and defined **input-output expectations**  
   - Created a **JSON dataset**, uploaded it to **S3**, and evaluated the model’s ability to generate structured recipes  

3. **Recipe Agent Configuration**  
   - Configured a **Titan Text G1-based agent** for structured input processing and recipe generation  
   - Developed functions:  
     - **ParseInput** to structure user input  
     - **GenerateRecipe** to generate recipes  
   - Organized tasks into **action groups**  
   - Validated the agent’s ability to process inputs and generate **detailed, actionable recipes**  

4. **API Integration with Lambda Function**  
   - Built a **Python-based AWS Lambda function** to handle HTTP requests and interact with Amazon Bedrock  
   - Set up an **API Gateway** with a **generate-recipe POST route** to allow external access  
   - Tested the API using **cURL requests**, confirming it successfully generated recipes (e.g., **Garlic Lemon Chicken**)  

### **Outcome:**  
You successfully developed a **fully serverless AI-powered recipe generation application**, integrating AWS services like Bedrock, S3, Lambda, and API Gateway.
