import xml.etree.ElementTree as etree

data = etree.parse('/Users/abhishekpradhan/Workspace/Github/Datasets/Ted Talk/ted_en-20160408.xml')

talks = data.getiterator(tag="file")

processed_talks_keywords = []
processed_talks_content = []
processed_talks_description = []
processed_talks_title = []

for talk in talks:
    keywords = []
    content = ""
    description = ""
    title = ""
    for tag in talk:
        if tag.tag=='head':
            for sub in tag:
                if sub.tag == 'keywords':
                    keywords = sub.text.split(",")
                    
                elif sub.tag == 'description':
                    description = sub.text.replace("\n"," ")

                elif sub.tag == 'title':
                    title = sub.text.replace("\n"," ")

        if tag.tag=='content':
            content = tag.text.replace("\n"," ")

        if keywords and content and description and title:
            processed_talks_keywords.append(keywords)
            processed_talks_content.append(content)
            processed_talks_description.append(description)
            processed_talks_title.append(title)


def save_to_file(file_path,list):
    thefile = open(file_path, 'w')
    for item in list:
      thefile.write("%s\n" % item)

print("Saving Content.....")
save_to_file("/Users/abhishekpradhan/Workspace/Github/TED-Talks/content.txt",processed_talks_content)
print("Saving Keywords.....")
save_to_file("/Users/abhishekpradhan/Workspace/Github/TED-Talks/keywords.txt",processed_talks_keywords)
print("Saving Description.....")
save_to_file("/Users/abhishekpradhan/Workspace/Github/TED-Talks/description.txt",processed_talks_description)
print("Saving Title.....")
save_to_file("/Users/abhishekpradhan/Workspace/Github/TED-Talks/title.txt",processed_talks_title)
print("Completed.....")
