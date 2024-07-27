# run python -m streamlit run "C:\Users\hussa\Desktop\testtest.py" to test

#create obj Speaker (holds for Speechbox) 
#(INPUT: string name, string imageURL, hexcode(?) color)
class Speaker:
  #define
  def __init__(self, name, imageURL, color):
    self.name = name
    self.imageURL = imageURL
    self.color = color

  #to string (used to display options for speaker)
  def __str__(self):
    return f"{self.name}, {self.color}"    
  
  def __eq__(self, other) : 
    if self.name == other.name \
    and self.imageURL == other.imageURL \
    and self.color == other.color:
        return True
    else:
        return False
  
  def editName(self, newName):
     self.name = newName
  def editImage(self, newImage):
     self.imageURL = newImage
  def editColor(self, newColor):
     self.color = newColor
  
#create obj Dialoguebox (for ocs' individual dialogue) 
#(INPUT: Speaker speaker, string dialogue)
class Dialoguebox:
    dialogueCode = ""

    #define
    def __init__(self, speaker, dialogue):
        self.speaker = speaker
        self.dialogue = dialogue

    #for getting the string
    def getDialogueCode(self):
        #text to return
        #rlly its speechbox start but whatever
        dialogueCode = '<!-- SPEECHBOX START -->\n	<div class="row no-gutters" style="margin: 10px 0px 10px 0px;">\n		<!-- icon -->\n		<!-- !!EDIT!! background-image url should be changed! -->\n		<div class="card col-md-2 col-4 p-1" style="border: none; \n		        border-radius: 25px;\n				overflow: hidden; \n				width: 100%; \n				min-height: 75px; \n				background-size: contain; \n				background-repeat: no-repeat;\n				background-position: center;\n				background-image:url(\'' + self.speaker.imageURL + '\');">\n		</div>\n		<!-- textbox -->\n		<div class="card col-md-10 col-8 p-1" style="border: none;">\n			<div class="bg-faded p-4 h-100" style="clip-path: polygon(0% 0%, 100% 0%, 100% 85%, 24% 85%, 0 100%, 10% 85%, 0% 85%);\n							margin-left: 20px; \n							border-radius: 5px; \n							min-height: 100px; \n                            border-top: 10px solid ' + self.speaker.color + '  ;">\n				<!-- !!EDIT!! text here! -->\n				<p align="center"> '+ self.dialogue +' </p>\n				<br>\n			</div>\n			<!-- !!EDIT!! replace self.speaker.color with whatever color u want-->\n			<div class="bg-faded p-12 h-100" style="\n                    							margin: -25px 0px 0px 0px; \n                    							margin-left: 70%;\n                    							background-color:  '+ self.speaker.color +'  ;\n                    							z-index: 10;\n                                                margin-left: auto;\n                                                width: 33%;\n                    							min-width: 25px;\n                    							max-width: 100px;\n							                    border-radius: 5px; \n							                    max-height: 25px;">\n				<!-- !!EDIT!! edit name here! -->\n				<p align="center">'+ self.speaker.name +'</p>\n			</div>\n		</div>\n	</div>\n'
        #print(dialogueCode)
        return dialogueCode

    #to string (to export as html file) (fix later lol)
    def __str__(self):
        return f"{self.speaker.name}: {self.dialogue}"  

#create obj AreaConvo (keep in list for overall editing, holds the dialogue between ocs)
#couldve been a list within a list tbh. But i love <3 objects
#(INPUT: string title)
class AreaConvo:
    #define
    listOfDialogue = []
    title = ""
    backimageURL = "Background image URL here"

    #forgot about this
    def editBackimageURL(self, imageURL):
        self.backimageURL = imageURL

    #button to add dialogueboxes
    def addDialogue(self, speaker, dialogue):
        self.listOfDialogue.append(Dialoguebox(speaker, dialogue))

    #button to remove dialogueboxes
    def removeDialogue(self, toindex):
        #self.listOfDialogue.remove(Dialoguebox(speaker, dialogue))
        self.listOfDialogue.pop(toindex)

    #button to edit dialogueboxes
    def editDialogue(self, toindex, speaker, dialogue):
        self.listOfDialogue[toindex] = Dialoguebox(speaker, dialogue)

    def moveUpDialogue(self, toindex):
        print(len(self.listOfDialogue))
        if (toindex >= 1) :
            print(self.listOfDialogue[toindex-1])
            toswap = self.listOfDialogue[toindex-1]
            print(toswap)
            self.listOfDialogue[toindex-1] = self.listOfDialogue[toindex]
            self.listOfDialogue[toindex] = toswap
        else:
            print("NO! Top of list")

            
    def moveDownDialogue(self, toindex):
        print(len(self.listOfDialogue))
        if (toindex < (len(self.listOfDialogue)-1)) :
            toswap = self.listOfDialogue[toindex+1]
            self.listOfDialogue[toindex+1] = self.listOfDialogue[toindex]
            self.listOfDialogue[toindex] = toswap
        else:
            print("NO! Bottom of list")
        

    def __init__(self):
        pass

    def __init__(self, title):
        self.title = title

    #not needed but i <3 __str__ function
    def __str__(self):
       #toreturn = "\n - ".join(str(x) for x in self.listOfDialogue)
       #return self.title.join(toreturn)
       return f"AREACONVO STRING - {self.title}" 
    
    #sortable items only work nicely with lists of strings
    #this returns the list as a list of strings
    #in the most annoying way possible <3
    def returnStrList(self):
        toreturn = self.listOfDialogue.copy()
        counter = 0
        for x in toreturn:
           toreturn[counter] = str(x)
           #print(toreturn[counter])
           counter = counter + 1 #im too c++pilled for this
       
        return toreturn
    
    import random
    areaConvoCode = ""
    toToggle = "a" + str(random.randint(1, 9999999999))

    def returnAreaConvoCode(self):
        toreturn = self.listOfDialogue.copy()
        counter = 0
        speechboxes = ""
        for x in toreturn:
           speechboxes = speechboxes + (toreturn[counter].getDialogueCode())
           #print(counter)
           #print(toreturn[counter].getDialogueCode())
           counter = counter + 1 #im too c++pilled for this
       
        speechboxes1 =  '<!-- !!EDIT!! -->\n		<!-- here all controls are denoted by ' + self.toToggle + '-->\n		<div>\n		    \n			<!--toggle visual -->\n		    <!-- !!EDIT!! edit background-image:url here -->\n			<div class="card p-3 mb-2" role="tab" id="headingclosed1" style="clip-path: polygon(8% 0, 100% 0%, 100% 100%, 8% 100%, 0% 50%); background-size: cover; background-position: center; background-image:url(\'' + self.backimageURL + '\'); text-align: right; border: none;">\n				<a data-toggle="collapse" data-parent="#allclosed" href="#' + self.toToggle + '" aria-expanded="false" aria-controls="' + self.toToggle + '">\n					<div class="mb-0">\n						<h2 style="text-shadow: #ddffb6 1px 0 10px; letter-spacing: 1px">\n							<span class="far" style="color: black;">' + self.title + '</span>\n						</h2>\n					</div>\n				</a>\n			</div>\n			\n			<!--content -->\n			<div id="' + self.toToggle + '" class="collapse" role="tabpanel" aria-labelledby="headingclosed1" data-parent="#allclosed">\n				<!-- DIALOGUE START --><div class="card" style="min-height:100px; \n				padding: 15px 25px 15px 35px;  \n				margin: 25px;">\n				\n				    <!-- !!EDIT!! paste dialogue code here :p -->\n				    ' +  speechboxes + '\n				\n				<!-- DIALOGUE END -->\n			</div>\n		</div>'       
        
        return speechboxes1
    
    def returnSingularAreaConvoCode(self):
        toreturn = self.listOfDialogue.copy()
        counter = 0
        speechboxes = '<div class="card" style="min-height:100px; \n				padding: 15px 25px 15px 35px;  \n				margin: 25px;">\n    \n	'
        for x in toreturn:
           speechboxes = speechboxes + (toreturn[counter].getDialogueCode())
           #print(counter)
           #print(toreturn[counter].getDialogueCode())
           counter = counter + 1 #im too c++pilled for this

        return speechboxes
    
# Main function to execute program
def main():
    #for debugging
    def debugListSpeakers():
        for x in st.session_state['listOfSpeakers']:
            print(x)
    print("Hello, how are you")

    #import
    import streamlit as st
    #from streamlit_sortables import sort_items

    #create default speakers 
    janeDoe = Speaker("Jane Doe", "Image.Url", "#6a6a6a") #default
    johnBrown = Speaker("John Brown", "Image.Url", "#FFFFFF") #default

    #check if theres any speakers already in session
    if 'listOfSpeakers' not in st.session_state:
        print("No speakers found in session!")
        st.session_state['listOfSpeakers'] = []
        st.session_state['listOfSpeakers'].append(janeDoe)
        st.session_state['listOfSpeakers'].append(johnBrown)
        print("Added speakers to session")

    #check if theres any areaconvos already in session
    if 'listOfAreaConvo' not in st.session_state:
        print("No area convos found in session!")
        defaultAreaConvo = AreaConvo("The beginning")
        defaultAreaConvo.addDialogue(st.session_state['listOfSpeakers'][0], "Hello world")
        st.session_state['listOfAreaConvo'] = []
        st.session_state['listOfAreaConvo'].append(defaultAreaConvo)

        #set default selection
        st.session_state['currentAreaConvoSelect'] = 0

        #create string list
        st.session_state['listOfAreaConvoTitles'] = st.session_state['listOfAreaConvo'].copy()
        counter = 0
        for x in st.session_state['listOfAreaConvoTitles']:
           st.session_state['listOfAreaConvoTitles'][counter] = x.title
           counter = counter + 1 

        print("Added area convo to session")

    #load speakers from session
    print("Loading speakers from session")
    debugListSpeakers()
    #st.session_state
    #LETS GOOO FIRST TRY (took me 10000 years to wrap my head around session state)
    
    st.header('PJSK Area Conversation Put-Togetherer', divider='violet')
    intro = '''hi!!!! this is an app to hopefully(?) make putting together the <a href='https://toyhou.se/26394659.pjsk-area-conversation-f2u'> pjsk area convo code</a> easier ^^  
    never used streamlit before but i hope it makes things slightly easier'''
    st.markdown(intro, unsafe_allow_html = True)

    notes = '''
    <b>notes:</b>
    - no i dont know why the buttons for rearranging the area convos are weird Sorry
    - unfortunately it does not save your work once u exit so u have to put it together all at once T_T
    - its kinda really scuffed so let me know if theres any bugs or weird things happening on <a href='https://toyhou.se/entomologist'>toyhou.se</a> or <a href='https://github.com/entomologist1'>github</a>'''
    st.markdown(notes, unsafe_allow_html = True)

    #display list of speakers
    st.header('Speaker Controls', divider='violet')
    with st.container(height=400, border=False):
        #basic markdown
        st.subheader('Add, remove, and edit your speakers here')

        #show list of speakers, current speaker, and its index
        selectSpeaker = st.selectbox("List of Speakers", st.session_state['listOfSpeakers'])
        #st.write("Current speaker:", selectSpeaker)
        selectSpeakerIndex = st.session_state['listOfSpeakers'].index(Speaker(selectSpeaker.name, selectSpeaker.imageURL, selectSpeaker.color))
        
        #create new speaker 
        with st.expander("Create new speaker"):
            createSpeakerName = st.text_input("New Speaker Name", placeholder="Name", key='createSpeakerName')
            createSpeakerImage = st.text_input("New Speaker Image Url", placeholder="Image URL", key='createSpeakerImage')
            createSpeakerColor = st.color_picker("New Speaker Color", "#ff5438", key='createSpeakerColor')

            #TODO: make it so that u cant submit empty speaker
            def submit_speaker_button():
                if (st.session_state.createSpeakerName):
                    if (st.session_state.createSpeakerImage):
                        st.session_state['listOfSpeakers'].append(Speaker(createSpeakerName, createSpeakerImage, createSpeakerColor))
                    else:
                        st.warning('CREATE SPEAKER ERROR: No image URL inputted', icon="⚠️")
                else:
                    st.warning('CREATE SPEAKER ERROR: No name inputted', icon="⚠️")

                print("Added new speakers, total below")
                debugListSpeakers()

            st.button('Submit new speaker', on_click=submit_speaker_button)

        #edit current speaker 
        with st.expander("Edit current speaker", expanded=True):
            col1name, col2image, col3color = st.columns(3)
            with col1name:
                st.markdown("<p style='text-align: center;'>edit name</p>", unsafe_allow_html=True)

                def nameChanged():
                    st.session_state['listOfSpeakers'][selectSpeakerIndex].editName(st.session_state.newEditSpeakerName)
                    debugListSpeakers()
                editSpeakerName = st.text_input("Edit:", selectSpeaker.name, key='newEditSpeakerName', on_change=nameChanged, help="Here, you can change the name of the speaker", label_visibility="hidden")
                #selectSpeaker

            with col2image:
                st.markdown("<p style='text-align: center;'>edit image</p>", unsafe_allow_html=True)

                def imageChanged():
                    st.session_state['listOfSpeakers'][selectSpeakerIndex].editImage(st.session_state.newEditSpeakerImage)
                    debugListSpeakers()
                editSpeakerImage = st.text_input("Edit:", selectSpeaker.imageURL, key='newEditSpeakerImage', on_change=imageChanged, help="Here, you can change the image of the speaker", label_visibility="hidden")
                
            with col3color:
                st.markdown("<p style='text-align: center;'>edit color</p>", unsafe_allow_html=True)

                def colorChanged():
                    st.session_state['listOfSpeakers'][selectSpeakerIndex].editColor(st.session_state.newEditSpeakerColor)
                    debugListSpeakers()
                editSpeakerImage = st.color_picker("Edit:", selectSpeaker.color, key='newEditSpeakerColor', on_change=colorChanged, help="Here, you can change the color of the speaker", label_visibility="hidden")
                
            def deleteCurrSpeaker():
                if (len(st.session_state['listOfSpeakers']) > 1):
                    st.session_state['listOfSpeakers'].pop(selectSpeakerIndex)
                else:
                    st.warning('DELETE SPEAKER ERROR: Cannot have empty list of speakers', icon="⚠️")
                debugListSpeakers()
            editSpeakerImage = st.button("Delete this speaker:", key='deleteSpeaker', on_click=deleteCurrSpeaker, help="Delete the current speaker")
                

    ######### area convo editing

    # test area conversation
    #areaconvo1 = AreaConvo("An example")
    #areaconvo1.addDialogue(st.session_state['listOfSpeakers'][0], "Ughhhhhhhhhhhhh")

    st.header('Area Conversation Controls', divider='violet')

    #overall area convo 
    #TODO Change sortable to selectable? T_T...
    st.subheader('Add, delete and reorder area conversations')
    #testArrangeAreaConvo = sort_items(st.session_state['listOfAreaConvoTitles'], direction='vertical', key='arrangeAreaConvo')
    
    testSelectboxArrangeAreaConvo = st.selectbox("Select area convo", st.session_state['listOfAreaConvoTitles'])
    #(testSelectboxArrangeAreaConvo)
    currentAreaConvoSelect = st.session_state['listOfAreaConvoTitles'].index(testSelectboxArrangeAreaConvo)
    #(currentAreaConvoSelect)

    st.session_state['listOfAreaConvoTitles']

    #test changes to area convo list
    #st.session_state['listOfAreaConvoTitles']
    #st.session_state['listOfAreaConvo']
    counter = 0
    for x in st.session_state['listOfAreaConvoTitles']:
        #st.session_state['listOfAreaConvoTitles'][counter]
        counter = counter + 1 

    with st.container(height=400, border=False):

        col1select, col2edit, col3adddel = st.columns(3)

        #TODO move current area convo up or down
        with col1select:
            st.markdown("<p style='text-align: center;'>move area convo</p>", unsafe_allow_html=True)
            #st.session_state['currentAreaConvoSelect'] = st.number_input("Insert a number", min_value=0, max_value=len(st.session_state['listOfAreaConvoTitles'])-1)
            #currentAreaConvoSelect = st.session_state['currentAreaConvoSelect']

        def moveUpCurrAreaConvo():
            print("Move up AreaConvo")

            if (currentAreaConvoSelect >= 1) :
                toswaptitle = st.session_state['listOfAreaConvoTitles'][currentAreaConvoSelect-1]
                st.session_state['listOfAreaConvoTitles'][currentAreaConvoSelect-1] = st.session_state['listOfAreaConvoTitles'][currentAreaConvoSelect]
                st.session_state['listOfAreaConvoTitles'][currentAreaConvoSelect] = toswaptitle

                toswap = st.session_state['listOfAreaConvo'][currentAreaConvoSelect-1]
                st.session_state['listOfAreaConvo'][currentAreaConvoSelect-1] = st.session_state['listOfAreaConvo'][currentAreaConvoSelect]
                st.session_state['listOfAreaConvo'][currentAreaConvoSelect] = toswap
            else:
                print("NO! Top of list")
                
        moveupAreaConvoBox = st.button("Move area convo up", key='moveUpAreaConvoButton', on_click=moveUpCurrAreaConvo, help="Move current area convo up")

        def moveDownCurrAreaConvo():
            print("Move down AreaConvo")

            if (currentAreaConvoSelect < (len(st.session_state['listOfAreaConvo'])-1)) :
                toswaptitle = st.session_state['listOfAreaConvoTitles'][currentAreaConvoSelect+1]
                st.session_state['listOfAreaConvoTitles'][currentAreaConvoSelect+1] = st.session_state['listOfAreaConvoTitles'][currentAreaConvoSelect]
                st.session_state['listOfAreaConvoTitles'][currentAreaConvoSelect] = toswaptitle

                toswap = st.session_state['listOfAreaConvo'][currentAreaConvoSelect+1]
                st.session_state['listOfAreaConvo'][currentAreaConvoSelect+1] = st.session_state['listOfAreaConvo'][currentAreaConvoSelect]
                st.session_state['listOfAreaConvo'][currentAreaConvoSelect] = toswap
            else:
                print("NO! Bottom of list")
                
        movedownAreaConvoBox = st.button("Move area convo  down", key='moveDownAreaConvoButton', on_click=moveDownCurrAreaConvo, help="Move current area convo down")



            
        #edit name of area convo
        with col2edit:
            st.markdown("<p style='text-align: center;'>edit area convo title</p>", unsafe_allow_html=True)
            def areaTitleNameChanged():
                    st.session_state['listOfAreaConvoTitles'][currentAreaConvoSelect] = (st.session_state.newEditAreaTitleName)
                    st.session_state['listOfAreaConvo'][currentAreaConvoSelect].title = (st.session_state.newEditAreaTitleName)
                    debugListSpeakers()
            editAreaTitleName = st.text_input("Edit Area Convo Title:", st.session_state['listOfAreaConvoTitles'][currentAreaConvoSelect], key='newEditAreaTitleName', on_change=areaTitleNameChanged, help="You can change the name of the area convo")

            def areaURLNameChanged():
                    st.session_state['listOfAreaConvo'][currentAreaConvoSelect].backimageURL = (st.session_state.newEditAreaURLName)
            editAreaURLName = st.text_input("Edit Area Convo URL:", st.session_state['listOfAreaConvo'][currentAreaConvoSelect].backimageURL, key='newEditAreaURLName', on_change=areaURLNameChanged, help="You can change the area convo's image URL")
            #st.session_state['listOfAreaConvo'][currentAreaConvoSelect].backimageURL

        #add or delete area convo
        with col3adddel:
            st.markdown("<p style='text-align: center;'>add or delete area convo</p>", unsafe_allow_html=True)

            def addCurrAreaConvo():
                defaultAddAreaConvo = AreaConvo("An example")
                defaultAddAreaConvo.addDialogue(st.session_state['listOfSpeakers'][1], " Ugh ")
                defaultAddAreaConvo.addDialogue(st.session_state['listOfSpeakers'][0], " Why the long face :D ")
                st.session_state['listOfAreaConvo'].append(defaultAddAreaConvo)
                st.session_state['listOfAreaConvoTitles'].append("An example")
            addAreaConvo = st.button("Add area convo:", key='addAreaConvo', on_click=addCurrAreaConvo, help="Add an area convo")
            
            def deleteCurrAreaConvo():
                if (len(st.session_state['listOfAreaConvo']) > 1) and (len(st.session_state['listOfAreaConvoTitles']) > 1) :
                    st.session_state['listOfAreaConvo'].pop(currentAreaConvoSelect)
                    st.session_state['listOfAreaConvoTitles'].pop(currentAreaConvoSelect)
                else:
                    st.warning('DELETE AREA CONVO ERROR: Cannot have empty list of area convos', icon="⚠️")
            delAreaConvo = st.button("Delete this area convo:", key='deleteAreaConvo', on_click=deleteCurrAreaConvo, help="Delete the current area convo")
                
    #CURRENT AREA CONVO
    currentAreaConvo = st.session_state['listOfAreaConvo'][currentAreaConvoSelect]

    st.subheader('Add, delete and reorder dialogues')
    #current dialogue selection

    #TODO remove this and replace for selectbox???? T_T T_T T_T
    #currentAreaConvo.listOfDialogue = sort_items(currentAreaConvo.returnStrList(), direction='vertical', key='arrangeDialogue')
    #st.write(f'sorted_items: {currentAreaConvo.listOfDialogue}')

    dialogueSelectTheIndex = st.selectbox("selectbox", range(len(currentAreaConvo.returnStrList())), format_func=lambda x: currentAreaConvo.returnStrList()[x])
    dialogueSelect = currentAreaConvo.returnStrList()[dialogueSelectTheIndex]

    st.write(currentAreaConvo.returnStrList() )
    
    with st.container(height=250, border=True):
            
        st.markdown("<p style='text-align: center;'>edit dialogue</p>", unsafe_allow_html=True)

        def dialogueContentChanged():
                    st.session_state['listOfAreaConvo'][currentAreaConvoSelect].editDialogue(dialogueSelectTheIndex, selectSpeakerCurrArea, (st.session_state.newEditDialogueContent))
                    #debugListSpeakers()
                    #It worked. I am free

        selectSpeakerCurrArea = st.selectbox("Speakers Available", st.session_state['listOfSpeakers'], help="sorry its rlly annoying but u have to edit the text before changes in speaker apply... iknow i know")
        #st.write("Current speaker:", selectSpeakerCurrArea)
        selectSpeakerIndexCurrArea = st.session_state['listOfSpeakers'].index(Speaker(selectSpeaker.name, selectSpeaker.imageURL, selectSpeaker.color))
        editDialogueContent = st.text_input("Edit text:", st.session_state['listOfAreaConvo'][currentAreaConvoSelect].listOfDialogue[0].dialogue, key='newEditDialogueContent', on_change=dialogueContentChanged, help="Hit enter to apply changes")



    col1edit, col2adddel = st.columns(2)
    with col1edit:
        st.markdown("<p style='text-align: center;'>reorder dialogue</p>", unsafe_allow_html=True)

        def moveUpCurrDialogue():
                print("Move up")
                st.session_state['listOfAreaConvo'][currentAreaConvoSelect].moveUpDialogue(dialogueSelectTheIndex)
                
        moveupDialogueBox = st.button("Move dialogue box up", key='moveUpDialogueButton', on_click=moveUpCurrDialogue, help="Move current dialogue box up")

        def moveDownCurrDialogue():
                print("Move down")
                st.session_state['listOfAreaConvo'][currentAreaConvoSelect].moveDownDialogue(dialogueSelectTheIndex)
                
        movedownDialogueBox = st.button("Move dialogue box down", key='moveDownDialogueButton', on_click=moveDownCurrDialogue, help="Move current dialogue box down")

        

    with col2adddel:
        st.markdown("<p style='text-align: center;'>add or delete dialogue</p>", unsafe_allow_html=True)

        def addCurrDialogue():
                st.session_state['listOfAreaConvo'][currentAreaConvoSelect].addDialogue(selectSpeakerCurrArea, "BLANK")
                
        addDialogue = st.button("Add dialogue box", key='addDialogueButton', on_click=addCurrDialogue, help="Add a dialogue box")

        def removeCurrDialogue():
                if ((len(currentAreaConvo.returnStrList())-1) > 0):
                    st.session_state['listOfAreaConvo'][currentAreaConvoSelect].removeDialogue(dialogueSelectTheIndex)
                else:
                    st.warning('AREA CONVO ERROR: Must have at least one dialogue box', icon="⚠️")

        removeDialogue = st.button("Remove dialogue box", key='removeDialogueButton', on_click=removeCurrDialogue, help="Remove current dialogue box")

            
    #dialogueSelectTheIndex
    #editing dialogues
    #dialogueSelect = st.selectbox("Select dialogue", currentAreaConvo.returnStrList())
    #(dialogueSelect)
    #display current area convo
    #(currentAreaConvo)
    #and the dialogues in it
    #st.write(currentAreaConvo.returnStrList())
    #st.write(currentAreaConvo.listOfDialogue)
    #st.write("list of area convo titles")
    #st.session_state['listOfAreaConvoTitles']
    #st.write("current selection")
    #st.session_state['listOfAreaConvoTitles'][currentAreaConvoSelect]

    #################################################

    st.header('Export your code', divider='violet')
    soloExport = st.checkbox("Only export current area conversation")

    if soloExport:

        areaConvoExportString = st.session_state['listOfAreaConvo'][currentAreaConvoSelect].returnSingularAreaConvoCode()
        toExportCode = st.text_area("Code here!", areaConvoExportString, height=600)

    else:

        listOfAreaConvoExport = st.session_state['listOfAreaConvo'].copy()
        listOfAreaConvoExportString = '<!-- encasing div -->\n<!-- me if overusing clip-path was illegal:  -->\n<div class="mx-auto" style="max-width:800px;">\n    \n	<!-- tab control -->\n	<div class="accordion md-accordion" id="allclosed" role="tablist" aria-multiselectable="true">\n	    \n		<!--i reccomend collapsing tabs/dialogues u arent working on cuz everything gets so confusing so quickly -->\n		<!--this is basically accordion collapse taken from https://toyhou.se/4547628.coding-resources-3 if u need resources -->\n		'
        counterLove = 0
        for x in listOfAreaConvoExport:
            print(listOfAreaConvoExport[counterLove])
            #st.write(listOfAreaConvoExport[counterLove])
            listOfAreaConvoExportString = listOfAreaConvoExportString + listOfAreaConvoExport[counterLove].returnAreaConvoCode()
            counterLove = counterLove + 1 
        
        listOfAreaConvoExportString = listOfAreaConvoExportString + '\n		\n		<!-- end encasing -->\n	</div>'

        toExportCode = st.text_area("Code here!", listOfAreaConvoExportString, height=600)




    

        

if __name__ == '__main__':
    main()
