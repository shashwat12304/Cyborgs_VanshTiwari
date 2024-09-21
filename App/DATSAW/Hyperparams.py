import cv2

class Hyperparams:
    def __init__(self):
        self.min_var = 0#(perfectly blurred)
        self.max_var = 320#(perfectly_fine)
        self.scores = [0.10,0.15, 0.33, 0.5, 0.66, 0.73,0.77, 0.80, 0.91, 0.96]

    def gamma(self,epsilon):
        return (round(epsilon, 1))*10

    def beta(self,epsilon):
        rounded_epsilon = round(epsilon, 1)
        if rounded_epsilon == 0:
            return 0.1
        beta = (1 -rounded_epsilon)*10
        return beta
    def Epsilon(self, path):
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        var_laplacian = cv2.Laplacian(gray, cv2.CV_64F).var()
        normalized_score = (var_laplacian - self.min_var) / (self.max_var - self.min_var)
        normalized_score = max(0, min(normalized_score, 1))
        return normalized_score

if __name__ == "__main__":
    h = Hyperparams()
    x = h.Epsilon(r"C:\Users\Shashwat.Sharma\Documents\cyborgs\VideoFrames\video1\frame_0.jpg")
    alpha = print('gamma:',h.alpha(x))
    beta = print('beta:',h.beta(x))
    delta = alpha+beta
    print('delta',delta)
    print('Epsilon',x)



