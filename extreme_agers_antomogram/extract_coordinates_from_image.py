import cv2 

img = cv2.imread('human_diagram.png', 1)
screen_res = (1280, 720)  # Example resolution
scale_width = screen_res[0] / img.shape[1]
scale_height = screen_res[1] / img.shape[0]
scale = min(scale_width, scale_height)

def click_event(event, x, y, flags, params): 
    if event == cv2.EVENT_LBUTTONDOWN: 

        print(x/scale, ' ', y/scale) 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(img, str(x) + ',' + str(y), (x, y), font, 1, (255, 0, 0), 2) 
        cv2.imshow('image', img) 
    if event == cv2.EVENT_RBUTTONDOWN: 
        print(x/scale, ' ', y/scale) 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        b, g, r = img[y, x] 
        cv2.putText(img, f'{b},{g},{r}', (x, y), font, 1, (255, 255, 0), 2) 
        cv2.imshow('image', img) 

if __name__ == "__main__": 
    window_width = int(img.shape[1] * scale)
    window_height = int(img.shape[0] * scale)
    
    img = cv2.resize(img, (window_width, window_height), interpolation=cv2.INTER_AREA)
    
    cv2.imshow('image', img) 
    cv2.setMouseCallback('image', click_event) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 