import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, LSTM, Concatenate
from tensorflow.keras.models import Model

class ModularAIComposer:
    """
    A class to design and implement modular and composable AI systems.
    """
    
    def __init__(self):
        """
        Initialize the ModularAIComposer class.
        """
        pass
    
    def build_perception_module(self, input_shape):
        """
        Build a perception module for processing sensory inputs.
        
        Args:
            input_shape (tuple): The shape of the input data.
        
        Returns:
            tensorflow.keras.Model: The perception module as a Keras model.
        """
        inputs = Input(shape=input_shape)
        x = Conv2D(32, (3, 3), activation='relu')(inputs)
        x = MaxPooling2D((2, 2))(x)
        x = Conv2D(64, (3, 3), activation='relu')(x)
        x = MaxPooling2D((2, 2))(x)
        x = Conv2D(64, (3, 3), activation='relu')(x)
        outputs = tf.keras.layers.Flatten()(x)
        
        model = Model(inputs=inputs, outputs=outputs)
        return model
    
    def build_reasoning_module(self, input_shape):
        """
        Build a reasoning module for processing high-level features and making decisions.
        
        Args:
            input_shape (tuple): The shape of the input features.
        
        Returns:
            tensorflow.keras.Model: The reasoning module as a Keras model.
        """
        inputs = Input(shape=input_shape)
        x = Dense(128, activation='relu')(inputs)
        x = Dense(64, activation='relu')(x)
        outputs = Dense(10, activation='softmax')(x)
        
        model = Model(inputs=inputs, outputs=outputs)
        return model
    
    def build_memory_module(self, input_shape):
        """
        Build a memory module for storing and retrieving information.
        
        Args:
            input_shape (tuple): The shape of the input sequences.
        
        Returns:
            tensorflow.keras.Model: The memory module as a Keras model.
        """
        inputs = Input(shape=input_shape)
        x = LSTM(128, return_sequences=True)(inputs)
        x = LSTM(64)(x)
        outputs = Dense(10, activation='softmax')(x)
        
        model = Model(inputs=inputs, outputs=outputs)
        return model
    
    def compose_modules(self, modules):
        """
        Compose multiple modules into a single AI system.
        
        Args:
            modules (list): A list of Keras models representing the modules to be composed.
        
        Returns:
            tensorflow.keras.Model: The composed AI system as a Keras model.
        """
        inputs = []
        outputs = []
        
        for module in modules:
            inputs.append(module.input)
            outputs.append(module.output)
        
        if len(outputs) > 1:
            combined_outputs = Concatenate()(outputs)
        else:
            combined_outputs = outputs[0]
        
        combined_inputs = inputs
        model = Model(inputs=combined_inputs, outputs=combined_outputs)
        return model
    
    def train_composed_model(self, model, train_data, epochs, batch_size):
        """
        Train the composed AI system on the given training data.
        
        Args:
            model (tensorflow.keras.Model): The composed AI system as a Keras model.
            train_data (tuple): A tuple of (x_train, y_train) representing the training data.
            epochs (int): The number of training epochs.
            batch_size (int): The batch size for training.
        """
        x_train, y_train = train_data
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size)
    
    def evaluate_composed_model(self, model, test_data):
        """
        Evaluate the performance of the composed AI system on the given test data.
        
        Args:
            model (tensorflow.keras.Model): The composed AI system as a Keras model.
            test_data (tuple): A tuple of (x_test, y_test) representing the test data.
        
        Returns:
            tuple: A tuple of (test_loss, test_accuracy) representing the evaluation metrics.
        """
        x_test, y_test = test_data
        test_loss, test_accuracy = model.evaluate(x_test, y_test)
        return test_loss, test_accuracy