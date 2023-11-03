from pyscript import document

  
def run_selections(event):
  
  text0_name4python = document.querySelector("#text0_name4python")
  text = text0_name4python.value

  text1_name4python = document.querySelector("#text1_name4python")
  prompt_topic = text1_name4python.value

  # Print ideal construction
    if prompt_topic == 'sentiment':
        prompt = f"""Identify the sentiment of the following text {text},
        output only a number from 1 to -1 where 1 means positive and -1 means negative. 
        Use the least number of words.""" 
        # 'Neutral (0)'  # without the "Use the least number of words."
        # '0'
        prompt_str = """Identify the sentiment of the following text {text},
        output only a number from 1 to -1 where 1 means positive and -1 means negative. 
        Use the least number of words."""
        
    elif prompt_topic == 'zeroshot':
        category0 = "statement"
        category1 = "question"
        category2 = "announcement"
        prompt = f"""Classify the following text 
        {text} as one of the categories: {category0}, {category1}, {category2}. 
        Use the least number of words."""
        # 'question'
        prompt_str = """Classify the following text 
        {text} as one of the categories: {category0}, {category1}, {category2}. 
        Use the least number of words."""
    
    elif prompt_topic == 'named_entity_recognition0':
        prompt = f"""Perform named entity recognition on the following text 
        {text} and identify a location, date, and person.""" 
        # 'Location: Not mentioned\nDate: Halloween Day'
        # 'Location: None\nDate: Halloween Day'
        prompt_str = """Perform named entity recognition on the following text 
        {text} and identify a location, date, and person.""" 
        
    elif prompt_topic == 'named_entity_recognition1':
        feature0 = "location"
        feature1 = "date"
        description0 = "location information"
        description1 = "date information"

        information_query = f"""perform named entity recognition"""
        # prompt = f"""Given the following text {text}, {information_query}:
        prompt = f"""Given the following text {text}, identify:
            {feature0}: {description0},
            {feature1}: {description1}
            Format the output as JSON with the following keys:
            {feature0},
            {feature1}"""
        # '{\n  "location": "Halloween Day",\n  "date": "Halloween Day"\n}'
        prompt_str = """Given the following text {text}, identify:
            {feature0}: {description0},
            {feature1}: {description1}
            Format the output as JSON with the following keys:
            {feature0},
            {feature1}"""
        
    elif prompt_topic == 'summarize':
        prompt = f"""Summarize the following text {text}"""
        # 'The text is asking if the recipient is open on Halloween Day.'
        prompt_str = """Summarize the following text {text}"""
        
    elif prompt_topic == 'translate':
        language = "french"
        prompt = f"""Translate the following text {text} to {language} language"""
        prompt_str = """Translate the following text {text} to {language} language"""
        
    elif prompt_topic == 'missing_wordORfillmask':
        # text_missing_word = "Are you open on Halloween [mask]?"
        out = text.split(" ")
        import numpy as np
        position = np.random.randint(low=0, high=len(out)-1, size=1)[0]
        out[position] = '[mask]'
        text_missing_word = ' '.join(out)
        prompt = f"""Given following text {text_missing_word}, what is the most logical word for 
        [mask] that completes the phrase. Return the completed phrase with the [mask] word filled in
        , use the least number of words."""
        # '"Given the context, the most logical word for [mask] in the phrase \'Are you open on Halloween [mask]?\' would be \'day\'."'
        # 'Are you open on Halloween night?'
        prompt_str = """Given following text {text_missing_word}, what is the most logical word for 
        [mask] that completes the phrase. Return the completed phrase with the [mask] word filled in
        , use the least number of words."""
        
    elif prompt_topic == 'dataset_creation0':
        # OpenAI example (https://platform.openai.com/examples): 
        information_query = "10 AI model names that were released" # "top science fiction movies"
        feature1 = "company"
        prompt = f"Create a two-column CSV of {information_query} along with the {feature1}."
        # 'AI Model Name, Company\n1. GPT-3, OpenAI\n2. BERT, Google\n3. ImageNet, Stanford\n4. ResNet, Microsoft\n5. AlphaGo, DeepMind\n6. Watson, IBM\n7. Siri, Apple\n8. TensorFlow, Google\n9. Caffe, Berkeley AI Research\n10. PyTorch, Facebook AI Research'
        prompt_str = "Create a two-column CSV of {information_query} along with the {feature1}."
        
    elif prompt_topic == 'dataset_creation1':
        from_year = 2022
        to_year = 2023
        feature0 = "model_name"
        description0 = f"""AI model name"""

        feature1 = "company"
        description1 = f"""Company name that created the model"""

        information_query = f"""List 10 AI models that were released"""

        prompt = f"""Given the following text {information_query}, identify:
            {feature0}: {description0},
            {feature1}: {description1}
            Format the output as JSON with the following keys:
            {feature0},
            {feature1}"""
        # 'Here are 10 AI models and their corresponding companies:\n\n1. GPT-3: OpenAI\n2. BERT: Google\n3. VGG16: Oxford University\n4. ResNet: Microsoft\n5. Transformer: Google\n6. AlexNet: University of Toronto\n7. Inception: Google\n8. U-Net: University of Freiburg\n9. YOLO: University of Washington\n10. GAN: NVIDIA\n\nFormatted as JSON:\n\n```json\n[\n  {\n    "model_name": "GPT-3",\n    "company": "OpenAI"\n  },\n  {\n    "model_name": "BERT",\n    "company": "Google"\n  },\n  {\n    "model_name": "VGG16",\n    "company": "Oxford University"\n  },\n  {\n    "model_name": "ResNet",\n    "company": "Microsoft"\n  },\n  {\n    "model_name": "Transformer",\n    "company": "Google"\n  },\n  {\n    "model_name": "AlexNet",\n    "company": "University of Toronto"\n  },\n  {\n    "model_name": "Inception",\n    "company": "Google"\n  },\n  {\n    "model_name": "U-Net",\n    "company": "University of Freiburg"\n  },\n  {\n    "model_name": "YOLO",\n    "company": "University of Washington"\n  },\n  {\n    "model_name": "GAN",\n    "company": "NVIDIA"\n  }\n]\n```'
        prompt_str = """Given the following text {information_query}, identify:
            {feature0}: {description0},
            {feature1}: {description1}
            Format the output as JSON with the following keys:
            {feature0},
            {feature1}"""
        
    elif prompt_topic == 'transform_question_into_a_statement':
        prompt = f"""Write the following question {text} as a statement, 
        start with 'The user would like to know'"""
        # 'The user would like to know if you are open on Halloween Day.'
        prompt_str = """Write the following question {text} as a statement, 
        start with 'The user would like to know'"""
        
    elif prompt_topic == 'text_similarity':
        prompt = f"""Summarize the following text {text}"""
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": "Respond concisely"},
            ]
        )
        statement1 = response['choices'][0]['message']['content']
        
        prompt = f"""Compute the word embeddings for {text} and {statement1}, compute the cosine
        similarity of the two word embeddings. Output the cosine
        similarity number only, do not output words."""
        # 'The cosine similarity of the two word embeddings is 0.694.'
        prompt_str = """Compute the word embeddings for {text} and {statement1}, compute the cosine
        similarity of the two word embeddings. Output the cosine
        similarity number only, do not output words."""
        
    elif prompt_topic == 'create_questions_based_on_a_text':
        import requests
        from bs4 import BeautifulSoup
        # 1) Get URL page
        inputurl = "https://en.wikipedia.org/wiki/Chatbot"
        page = requests.get(inputurl)

        # Scrape webpage : soup is the html document
        soup = BeautifulSoup(page.content, 'html.parser')

        # Get all the paragraphs of text
        page = soup.find_all('p')
        scrapped_text = page[1].getText()

        prompt = f"Write 5 questions based on the text below\n\nText: {scrapped_text}\n\nQuestions:\n1."
        # 'What is a chatbot and what is its purpose? \n2. How do modern chatbots utilize artificial intelligence in their interactions with users? \n3. What techniques are often used in the development of chatbot technologies? \n4. Have chatbots been in existence for a long time? \n5. How do chatbots interact with users - through text, voice, or both?'
        prompt_str = "Write 5 questions based on the text below\n\nText: {scrapped_text}\n\nQuestions:\n1."
        
    elif prompt_topic == 'weekday_number':
        prompt = f"""Perform named entity recognition on the following text 
        {text} and identify a location and date."""
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
                {"role": "assistant", "content": "Respond concisely"},
            ]
        )
        parse_out = response['choices'][0]['message']['content']
        date_text = parse_out.split('Date: ')[-1]

        prompt = f"""What weekday is {date_text} from today's date using year 2023,
        use the the least number of words and show the weekday name converted to a number, 
        output the number."""
        # 'Halloween Day in 2023 is on a Tuesday.\nThe weekday number is 2.'

        # prompt = f"""What weekday is {date_text} from today's date using year 2023,
        # convert the weekday name to a number and output only the number. Use the the least number of words"""
        # 'Halloween in 2023 is on a Tuesday. The corresponding number for Tuesday is 2.'
        prompt_str = """What weekday is {date_text} from today's date using year 2023,
        use the the least number of words and show the weekday name converted to a number, 
        output the number."""
      
  # -------------------------------------

  if document.querySelector("#rad1").checked:
      which_model == 'gpt-4'
      # system = a message to help set the behavior of the assistant
      system_content = "You are a helpful assistant"
      #system_content = "You are a helpful assistant that responds with ? if the information is unknown."

      # assistant = stores previous assistant responses AND/OR it can be text to give examples the of desired response
      # (a request about how to organize the responses) [can modify response AND/OR organization of response]
      assistant_content = "Respond concisely"
      
      response = openai.ChatCompletion.create(
          model=model,
          messages=[
              {"role": "system", "content": system_content},
              {"role": "user", "content": prompt},
              {"role": "assistant", "content": assistant_content},
          ]
      )
      parse_out = response['choices'][0]['message']['content']
    
  elif document.querySelector("#rad2").checked:
      which_model == 'gpt-3.5-turbo'
      # system = a messageto help set the behavior of the assistant
      system_content = "You are a helpful assistant"
      #system_content = "You are a helpful assistant that responds with ? if the information is unknown."

      # assistant = stores previous assistant responses AND/OR it can be text to give examples the of desired response
      # (a request about how to organize the responses) [can modify response AND/OR organization of response]
      assistant_content = "Respond concisely"
      
      response = openai.ChatCompletion.create(
          model=model,
          messages=[
              {"role": "system", "content": system_content},
              {"role": "user", "content": prompt},
              {"role": "assistant", "content": assistant_content},
          ]
      )
      parse_out = response['choices'][0]['message']['content']
  
  elif document.querySelector("#rad3").checked:
      which_model == 'davinci-002'
      # Updated base models (2023)
      response = openai.Completion.create(model=model, prompt=prompt, temperature=0, max_tokens=20, top_p=1, n=1, logprobs=2)

      # Print text response only
      parse_out = response.choices[0]['text']
      
  elif document.querySelector("#rad4").checked:
      which_model == 'babbage-002'
      # Updated base models (2023)
      response = openai.Completion.create(model=model, prompt=prompt, temperature=0, max_tokens=20, top_p=1, n=1, logprobs=2)

      # Print text response only
      parse_out = response.choices[0]['text']
      
  elif document.querySelector("#rad5").checked:
      which_model == 'text-davinci-003'
      # Legacy models (2020–2022)
      model = "text-davinci-003"
      response = openai.Completion.create(model=model, prompt=prompt, temperature=0, max_tokens=20, top_p=1, n=1, logprobs=2)
      # Print text response only
      parse_out = response.choices[0]['text']

  # -------------------------------------

  output_div = document.querySelector("#output")
  output_text = {"OpenAImodel": {which_model}, "modelOutput": {parse_out}, "ReliablePromptconstruction": {prompt_str}}
  output_div.innerText = output_text

  # -------------------------------------
