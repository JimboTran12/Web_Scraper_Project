from openai import OpenAI
client = OpenAI()


class AI:
    def __init__(self, files, output_dir):
        self.files = files
        self.output_dir = output_dir

    def generate(self):
        for count, file in enumerate(self.files, start=1):
            with open(file, "r") as out_file:
                header = out_file.readline()
                prompt = "The article is " + out_file.read()
                completion = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                    {"role": "assistant", "content":  prompt},
                    {"role": "user", "content": "Please make the article concise, up to 50 words"}
                    ]
                    )
                content = completion.choices[0].message.content
                with open(self.output_dir + "/url" + str(count) + ".txt","w") as f:
                    f.write(header + "\n" + content)

        


