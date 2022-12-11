import sys
import openai

openai.api_key = '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'

prompt_text = '''
Summarize the following transcript. Write using the following format. Replace everything in <> brackets.

        Main Points:
        - <main point 1> : by <speaker 1>
        - <main point 2> : by <speaker 2>
        - <and so on> : by <and so on>

        Action Items:
        - <action 1> : by <speaker 1>
        - <action 2> : by <speaker 2>
        - <and so on> : by <and so on>

        Highights: 
        - <highlight 1>
        - <highlight 2>
        - <and so on>

        Recent Summary: 
        <short summary of the transcript>

        Transcript:

18:29:55 - You:
 Hi, welcome to the meeting. here, I'm going to discuss some Italian points about gpt3. In this call. And also going to mention some action items. For executing this project.

18:30:26 - You:
Yeah. so with more than 2 decades of x experience in the application, lifecycle management space, on the regularly, help companies with their digital transformation by using their sort of products, given the fact that the, we are an agile team and the use can then And the chaos way of working. Standard calls are really important to us and in fact, you wake up in one of our employees at midnight, they will swear an oath of legions to the stand-up call. The other thing we saw by his matrix, observable metrics like burndown charts etc are one thing They have been doing that for a for so long. Yeah, good at it. How about qualitative metrics? How do you measure the qualitative stuff like team, cohesion teams and sentiment objective priority, and then use them to manage projects. Daily stand. Up calls are an excellent way of capturing this information. the COVID-19 forcing us to move, all start of meetings, to zoom, hang outs and Microsoft teams, it became an opportunity for us to explore these use cases, The first step to attempting, those large problem is to capture the summary of the meeting. What we describe. Next is a local experiment, we conducted and it results by using Google Speech to text and gpt3. so what we do is the breakdown, the problem into three broad steps, one is transcribe the audio Um, Given that all the speech is over multiple channels. We found that Google TTS engine did an excellent job. to run rapid experiments, we chose to use a chrome extension need and scripts which dumps that and script of the entire conversation into a Google word talk. For further processing, We chose a sample from our daily calls for this experiment. And then be three process. The text all our visions and reprocessing work to improve performance of subsequent steps, other than the usual, special character removal nonsense. Word removal. Um, There were other steps that we have included in our code. It's funny that for most for something, that is a privy, think a lot more about it in post. And then we run the, the summary using gpt3. This is what typically shines given a meeting transcript, because he doesn't see engine cannot extract relevant. Details, that can be acted upon anything. That means that we are not just looking at a summary button who button proper actionable summary. What follows is a discussion of experiment and subsequent results. We have like kids with shiny toys after the first experiment. We want to take gp3 out for a ride with zero pre-work. That means that we wanted to understand how robust the solution was in its official state. The STD engine itself was itself a source of error, but we found the jbt was able to overcome this problem at first glance. Um, we give the typical status stand up, would involve a lead, directing the flow of the conversation. With each team member giving his work update in done. We took such an extract from the transcript of our own team picture below. It is a 600 words transcript, which is filled with broad updates on the AI products that that we worked on the day before. He then asked gp3 to summarize, this text asus the DaVinci engine um, there are team as well. Well, working on the first release of the radio app and now waiting for approval from the red desk representative that emails also working on care on for next release. That is awesome. We were able to condense our conversation from 500 word to just 50 words without Mom much work, but there is an issue. The thing with the minutes of making is to capture who did what extremely well. These details are important so that one can create assign the work to create an assign the work. What we have is good for an email but not something. We can perform subsequent processing online, agile card creation card moment on this one board and etc.
'''

engines = openai.Engine.list()
print(engines.data)
completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt_text, max_tokens=916)
print(completion.choices[0].text)