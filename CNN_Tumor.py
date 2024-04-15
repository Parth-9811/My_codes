import pandas as pd
import numpy as np
import keras
from keras.models import *
from keras.layers import *
from keras.optimizers import *
from keras.callbacks import *
import seaborn as sns
import matplotlib.pyplot as plt
import pandas.util.testing as tm
from sklearn import *
from sklearn.model_selection import *
from sklearn.preprocessing import *

cancer = datasets.load_breast_cancer()
#print(cancer.DESCR)
X = pd.DataFrame(data = cancer.data, columns=cancer.feature_names)
#print(X.head())
y = cancer.target
#print(y)
#print(cancer.target_names)
np.array(['malignant', 'benign'], dtype='<U9')
#print(X.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0, stratify = y)

#print(X_train.shape)
#print(X_test.shape)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

X_train = X_train.reshape(455,30,1)
X_test = X_test.reshape(114, 30, 1)

epochs = 50
model = Sequential()
model.add(Conv1D(filters=32, kernel_size=2, activation='relu', input_shape = (30,1)))
model.add(BatchNormalization())
model.add(Dropout(0.2))

model.add(Conv1D(filters=64, kernel_size=2, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))

model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(1, activation='sigmoid'))
#print(model.summary())

model.compile(optimizer=Adam(lr=0.00005), loss = 'binary_crossentropy', metrics=['accuracy'])
history = model.fit(X_train, y_train, epochs=epochs, validation_data=(X_test, y_test), verbose=1)

def plot_learningCurve(history, epoch):
  # Plot training & validation accuracy values
      epoch_range = range(1, epoch+1)
      plt.plot(epoch_range, history.history['accuracy'])
      plt.plot(epoch_range, history.history['val_accuracy'])
      plt.title('Model accuracy')
      plt.ylabel('Accuracy')
      plt.xlabel('Epoch')
      plt.legend(['Train', 'Val'], loc='upper left')
      plt.show()

      # Plot training & validation loss values
      plt.plot(epoch_range, history.history['loss'])
      plt.plot(epoch_range, history.history['val_loss'])
      plt.title('Model loss')
      plt.ylabel('Loss')
      plt.xlabel('Epoch')
      plt.legend(['Train', 'Val'], loc='upper left')
      plt.show()

history.history
plot_learningCurve(history, epochs)