def sets_creation(df, first_threshold, ratio):
    #simple method
    training_set = df[:first_threshold]
    test_set = df[first_threshold:]
    
    #dynamical method
    training_set_threshold = int(len(df)*ratio)

    training_set = df[:training_set_threshold]
    test_set = df[training_set_threshold:]
    print("training_set size", len(training_set))
    print("test_set size", len(test_set))
    
    return training_set, test_set
