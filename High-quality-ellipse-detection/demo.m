%%��ȡ�ļ�
%�������ļ�
sourcepath='D:\studyhard\����\BicycleBehaviorAnalysis-master\yolo3_deepsort\model_data\Road Bicycle Race.mp4';
outpath='test.avi';
loc=dlmread('detection.txt');

fps=30;
obj=VideoWriter(outpath);
obj.FrameRate=fps;
open(obj);
startframe=1;

source=VideoReader(sourcepath);
endframe=1000
%endframe=source.NumberOfFrames;
%ѭ������
set(0,'DefaultFigureVisible', 'off')
for i =startframe:endframe
    frame=read(source,i);
    cap=LCS_ellipse(frame,loc(i));
    writeVideo(obj,cap.cdata);
end
close(obj)
