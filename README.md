# doc_denoiser
OCR becomes a fast growing and needed technique nowadays. One of its application is process scanned images, But here we encounter a challenge. This challenge is the scanner noise, from salt and pepper noise to background noise. This solution aims to deenoise scanned text images to preprocess them for more reliable and accurate OCR applications.
I used 5*5 convolutional kernel (after falttening it to a 25d feature vector) to extract feature from training samples with sampling probability 0.02. and then train the Random forest algorithm for predicting the center of the same kernel applied to a cleaned version of the training image.
The dataset is downloaded from kaggle.
