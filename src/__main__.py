import cv2
import os
import argparse

class Video2Picture():
    def __init__(self, video_file, output_path, frame) -> None:
        if output_path is None:

            base_path = os.path.dirname(video_file)
            basename = os.path.basename(video_file)
            file_name = os.path.splitext(basename)[0]
            output_path = os.path.join(base_path, "pic_" + file_name)

        self.video_file = video_file
        self.output_path = output_path
        self.frame = frame
        pass


    def Convert2Picture(self):
        os.makedirs(self.output_path, exist_ok=True)
        vc = cv2.VideoCapture(self.video_file)
        c = 0
        if vc.isOpened():
            rval, frame = vc.read()
        else:
            rval = False

        while rval:
            rval, frame = vc.read()
            base_save_path = self.output_path + '\\'
            if (c % self.frame == 0):
                output_file = base_save_path + str(c) + '.jpg'
                cv2.imencode('.jpg', frame)[1].tofile(output_file)
            c = c + 1
            cv2.waitKey(1)
        vc.release()
    
def main():
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-i", "--video_file", help="video input file, ex: C:\\test.mov", required=True)
    argParser.add_argument("-o", "--output_path", help="picture output path, ex: C:\\test")
    argParser.add_argument("-f", "--frame", type=int, help="catch per frame, ex: 30", required=True)
    args = argParser.parse_args()

    video_file = args.video_file
    output_path= args.output_path
    frame= args.frame
    obj = Video2Picture(video_file, output_path, frame)
    obj.Convert2Picture()
    pass

if __name__ == "__main__":
    main()