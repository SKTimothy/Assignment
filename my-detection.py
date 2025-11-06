import jetson_inference
import jetson_utils
from datetime import datetime

net = jetson_inference.detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = jetson_utils.videoSource("/dev/video0")
display = jetson_utils.videoOutput("display://0")

log_file = f"detection_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
log = open(log_file, "w")

count = 0
while display.IsStreaming() and count < 20:
    img = camera.Capture()
    if img is None: continue
    detections = net.Detect(img, overlay="box,labels,conf")
    if detections:
        d = detections[0]
        msg = f"\n--- Detection {count+1} ---\n"
        msg += f"ClassID:     {d.ClassID}\n"
        msg += f"Confidence:  {d.Confidence:.6f}\n"
        msg += f"Left:        {d.Left:.3f}\n"
        msg += f"Top:         {d.Top:.3f}\n"
        msg += f"Right:       {d.Right:.3f}\n"
        msg += f"Bottom:      {d.Bottom:.3f}\n"
        msg += f"Width:       {d.Width:.3f}\n"
        msg += f"Height:      {d.Height:.3f}\n"
        msg += f"Area:        {d.Area:.3f}\n"
        msg += f"Center:      ({d.Center[0]:.3f}, {d.Center[1]:.3f})\n"
        print(msg)
        log.write(msg)
        jetson_utils.saveImage(f"detection_{count+1}.jpg", img)
        count += 1
    display.Render(img)
    display.SetStatus(f"Detections: {count}/20 | FPS: {net.GetNetworkFPS():.1f}")

log.close()
print(f"Log saved: {log_file}")
