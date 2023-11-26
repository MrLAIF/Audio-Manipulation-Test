from pydub import AudioSegment

AudioSegment.converter = "ffmpeg.exe"


def cutInIntervals(inFile, outDirectory, segmentLength=10):
    audio = AudioSegment.from_file(inFile)
    
    #Calculate the total lenght of the audio in ms
    totalDuration = len(audio)
    
    #Calculate the number of segments
    numSegments = totalDuration // (segmentLength * 1000)
    
    #Cut the audio and then export it
    for i in range(numSegments):
        startTime = i * segmentLength * 1000
        endTime = (i + 1) * segmentLength * 1000
        
        print(i)

        #If it's the last iteration, segment from the last end time to the end of the audio
        if i+1==numSegments:
            segment = audio[startTime:totalDuration]
        else:
            segment = audio[startTime:endTime]

        #Exports the file and names it after the iteration
        segment.export(f"{outDirectory}/segment-{i + 1}.mp3", format="mp3")



inFile = "All I Want for Christmas Is You.mp3"
#By default the audio is cut in 10sec sections, in this example it's cut in 30sec sections
cutInIntervals(inFile,"Segments",30)