## Inspiration
There are many students who do not have chance to learn and study in classes. Teachers may also have trouble developing plans to teach in class. Thus, we would like to build a platform that offers free education services for teachers and students. 

## What it does
There are four services that we built:
- First is Generating Teaching Content Plan by asking teachers Input different criteria and AI will generate teaching content for teachers. 
- Second is Teaching Images Generator, Teachers Input teaching image criteria for AI to generate needed images for teaching slides. 
- Third service is Searching Knowledge about Python, Students search information about Python in the database through chatting with AI. 
- Finally is Learning Python through Talking. Students talk and discuss with AI to learn Python.

## How we built it
- First teachers can generate teaching content by putting in different criteria as prompts for Open AI LLM to generate a plan for teaching the subject. This function was built using Python and Open AI LLM. 
- Further, teachers can generate teaching images by putting prompts input which is sent to DALL-E  to generate the images. This function was built using Python and DALL-E. 
- Students can talk with  AI to learn more about a certain subject which was developed using  Azure OpenAI API credentials, along with Azure’s Speech-to-Text and Text-to-Speech services.
- Finally, students can use  Azure Open AI Search to search for knowledge about certain subjects like Python. This function was developed using Azure Cosmos DB, Custom Data, Retrieval Augmented Generation pattern, Azure OpenAI Service, Azure AI Search for data indexing and retrieval, and Azure Document Intelligence with Optical Character Recognition.

## Challenges we ran into
We had challenges to learn all new functions of Azure Open AI. It took us some time to learn and become familiar with different Azure AI services, designed, built, and then debugged all the errors to bring the app to life.

## Accomplishments that we're proud of
We were able to build different functions using various Azure Open AI services such as images, text, and speech. We were able to use features such as  Azure Cosmos DB, Retrieval Augmented Generation pattern, Azure OpenAI Service, Azure AI Search for data indexing and retrieval, and Azure Document Intelligence with Optical Character Recognition. 

## What we learned
We learnt to build different functions using Azure Open AI such as:
- Generating text using Azure Open AI
- Generating text using Azure DALL-E
- Develop Speech-to-Text and Text-to-Speech services in combination with Azure Open AI
- Develop App using Cosmos DB, Custom Data, Retrieval Augmented Generation pattern, Azure OpenAI Service, Azure AI Search for data indexing and retrieval, and Azure Document Intelligence with Optical Character Recognition.

## Responsible AI
- Fairness: The app treats all people fairly
- Reliability and safety: The app performs reliably and safely
- Inclusiveness: The app empowers and engages everyone who is student to learn and improve themselves.
- Transparency: The app is understandable and easy to use.
- The app was tested and tested multiple times to make sure the AI system is working as intended and can be trusted.

## What's next for Learnology
- We want to add more Custom Data to teach students about different subjects
- We want the speech services to be indifferent languages other than English

