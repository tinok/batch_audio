import os
import transcription_analysis.engine as engine

i = 0

for filename_old in os.listdir('audio_files'):
	filename, file_extension = os.path.splitext(filename_old)
	transcriptionfile = './transcribed_audio_files/'+filename+'.txt'
	if os.path.isfile(transcriptionfile):
		pass
	else:
		file = './audio_files/'+filename+file_extension
		print(file)
		engine.handle_audio_transcription_request(file, 'es-CO')
		i += 1
		print('Transcription Completed for file '+str(i)+'.')
