def model(self):
    network = input_data(shape=[None, 4, 1], name='input')
    network = fully_connected(network, 1, activation='linear')
    network = regression(network, optimizer='adam', learning_rate=self.lr, loss='mean_square', name='target')
    model = tflearn.DNN(network, tensorboard_dir='log')
    return model
def train_model(self, training_data, model):
    X = np.array([i[0] for i in training_data]).reshape(-1, 4, 1)
    y = np.array([i[1] for i in training_data]).reshape(-1, 1)
    model.fit(X,y, n_epoch = 1, shuffle = True, run_id = self.filename)
    model.save(self.filename)
    return model

