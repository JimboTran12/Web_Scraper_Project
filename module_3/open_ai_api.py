from openai import OpenAI

"""
AI class process each of its text files 
by using openAI API write a concise versions
of them and save them into a desfinated
directory
"""

class AI:
    def __init__(self, files, output_dir):
        self.files = files   #save text files
        self.output_dir = output_dir #directory where the generated files will be stored

    def generate(self):
        client = OpenAI()
        for count, file in enumerate(self.files, start=1):
            with open(file, "r", encoding='utf-8') as out_file:
                header = out_file.readline()  # Save the headline and leave the body to use as the prompt
                prompt = "The article is " + out_file.read()
                completion = client.chat.completions.create( #API call
                    model="gpt-3.5-turbo",
                    messages=[
                    {"role": "assistant", "content":  prompt},
                    {"role": "user", "content": "Please make the article concise, up to 50 words"}
                    ]
                    )
                content = completion.choices[0].message.content #response message saved
                with open(self.output_dir + "/url" + str(count) + ".txt","w") as f:
                    f.write(header + "\n" + content) #Write headline and reponse message to a new text file in designated folder

        


