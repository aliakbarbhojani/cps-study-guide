'''
This is a project that combines CPS 109 and CPS 213 content into one project. 

The project is designed using the fundamental python conceps covered in CPS 109 upto classes.
All the topics covered in CPS 213 are included in a JSON file with all the details and explanations of each topic.
Using the JSON file, the project will integrate it into python and create a simple command line interface to learn and explore the 213 topics.

Essentially, the project is a learning tool to learn CPS 213 and combines python form CPS 109 to create this simple project!
'''
#Module imports
import os
import random
import json

#Open the JSON file and load the data into a python dictionary
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

#Class to represent a topic and its associated information
class Topic:
    #Initialize the topic with its attributes
    def __init__(self, id, title, summary, key_points, worked_example, visual, study_tip, learn_more):
        self.id = id
        self.title = title
        self.summary = summary
        self.key_points = key_points
        self.worked_example = worked_example
        self.visual = visual
        self.study_tip = study_tip
        self.learn_more = learn_more

    #Display the topic menu and prompt the user to select a topic
    def topic_menu(self):
        print("""\nTopic Menu:
        \n01 - Numbering Systems
        \n02 - Number System Conversions
        \n03 - Signed Number Representations
        \n04 - Representable Value Ranges
        \n05 - Signed and Unsigned Representation
        \n06 - Signed Arithmetic
        \n07 - Logic Gates
        \n08 - Tri-State Buffers
        \n09 - Timing Diagrams
        \n10 - Boolean Algebra Simplification
        \n11 - Boolean Algebra Identities
        \n12 - Operator Precedence
        \n13 - Circuit Simplification
        \n14 - Minterms and Maxterms
        \n15 - Canonical SOP and POS
        \n16 - Truth Tables from Canonical Forms
        \n17 - DeMorgan's Law and Simple Gates
        \n18 - NAND-NAND and NOR-NOR Conversion
        \n19 - Truth Tables to K-Maps
        \n20 - K-Map Adjacency and Grouping
        \n21 - 2-Variable SOP K-Maps
        \n22 - 2-Variable POS K-Maps
        \n23 - 3- and 4-Variable K-Maps
        \n24 - K-Maps with Don't-Care Conditions
        \n25 - Half-Adder vs Full-Adder
        \n26 - 2-Bit Adder
        \n27 - 4-Bit Adder
        \n28 - 4-Bit Adder/Subtractor
        \n29 - 2-Bit Magnitude Comparator
        \n30 - Decoders
        \n31 - Encoders
        \n32 - Multiplexers
        \n33 - Arithmetic Logic Unit (ALU)
        \n34 - Latches
        \n35 - Flip-Flops
        \n36 - State Diagrams
        \n37 - State Diagram to Circuit
        \n38 - Register Circuits
        \n39 - Synchronous Counter Design
        \n40 - Serial / Shift Registers""")

        #Prompt the user to select a topic number and validate the input
        while True:
            try:
                topic = int(input("\nEnter your option (1-40): "))

                if topic < 1 or topic > 40:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 40.")
                continue
            
            return topic

    #Get the topic details from the JSON data based on the selected topic number
    def get_topic(self, data, selected_topic):
        zfill_topic = str(selected_topic).zfill(2)

        #Search for the topic in the JSON data and return a Topic object if found
        for topic in data["topics"]:
            if topic["id"] == zfill_topic:
                return Topic(
                    id=topic["id"],
                    title=topic["title"],
                    summary=topic["summary"],
                    key_points=topic["key_points"],
                    worked_example=topic["worked_example"],
                    visual=topic["visual"],
                    study_tip=topic["study_tip"],
                    learn_more=topic["learn_more"]
                )
        return None

    #Display the topic information
    def learn_topics(self):
        print("\n" + "=" * 60)
        print(f"  TOPIC {self.id}: {self.title.upper()}")
        print("=" * 60)

        # Summary
        print("\n📘 SUMMARY")
        print("-" * 60)
        print(self.summary)

        # Key Points
        print("\n💡 KEY POINTS")
        print("-" * 60)
        for point in self.key_points:
            print(f"  • {point}")

        # Worked Example
        print("\n✏️ WORKED EXAMPLE")
        print("-" * 60)
        print(self.worked_example)

        # Visual
        print("\n👁️ VISUAL")
        print("-" * 60)

        if isinstance(self.visual, dict):
            print(
                self.visual.get(
                    "description",
                    "No visual description available."
                )
            )

            if self.visual.get("recommended_file"):
                print(f"\n  Image file: {self.visual['recommended_file']}")
        else:
            print(self.visual)

        # Study Tip
        print("\n🎯 STUDY TIP")
        print("-" * 60)
        print(self.study_tip)

        # Learn More
        print("\n🔗 LEARN MORE")
        print("-" * 60)

        if isinstance(self.learn_more, list):
            for index, resource in enumerate(self.learn_more, start=1):
                print(f"\n  {index}. {resource.get('title', 'Untitled resource')}")
                print(f"     Type: {resource.get('type', 'Not specified')}")
                print(f"     URL:  {resource.get('url', 'No URL available')}")
        else:
            print(self.learn_more)

        print("\n" + "=" * 60)

# Main program execution        
if __name__ == "__main__":

    # Load the JSON data from the file
    json_file = os.path.join(
        os.path.dirname(__file__),
        "cps213_study_guide.json"
    )

    data = load_json(json_file)

    #Start the main loop to display the menu and handle user input
    while True:
        print("""\n Options:
        1. Learn topics
        2. Random Facts
        3. Exit""")
        
        try:
            option = int(input("\nEnter your option (1-3): "))
        
            if option < 1 or option > 3:
                raise ValueError
            
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue

        #Handle the user's menu selection
        if option == 1:
            topic = Topic(None, None, None, None, None, None, None, None)
            topic_number = topic.topic_menu()
            topic_content = topic.get_topic(data, topic_number)

            if topic_content:
                topic_content.learn_topics()
            else:
                print("Topic not found.")

        #Display a random fact
        elif option == 2:
            random_fact = random.choice(data["random_facts"])
            print("\n" + "=" * 60)
            print("  RANDOM FACT")
            print(f" • {random_fact['fact']}")
            print("=" * 60)

        #Exit the program
        elif option == 3:
            print("Exiting the program.")
            break

        #Handle invalid menu selection
        else:
            print("Invalid option. Please try again.")