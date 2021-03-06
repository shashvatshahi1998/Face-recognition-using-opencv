image_size = 28
pixel_depth = 255

def load_letter(folder,min_num_Pages):

    image_files = os.listdir(folder)
    dataset = np.ndarray(shape=(len(image_files),image_size,image_size,dtype=np.float32))
    print(folder)
    num_images = 0
    for image in image_files:
        image_file = os.path.join(folder,image)
        try:
            image_data = (imageio.imread(image_file).astype(float) - pixel_depth/2)/pixel_depth

            if image_depth != (image_size,image_size):
                raise Exception('Unexpected image shape: %s' % str(image_data.shape))
            dataset[num_images,:,:] = image_data
            num_images = num_images+1
        except(IOError,ValueError) as e:
            print('Could not read:',image_file,':',e,'-it\'s ok,skipping.')

    dataset = dataset[0:num_images,:,:]
    if num_images < min_num_images:
        raise Exception('Many fewer images: %d < %d' % (num_images,min_num_images))

    print('Full dataset tensor:', dataset.shape)
    print('Mean:', np.mean(datset))
    print('Standard Deviation:', np.std(dataset))

    return dataset
    
def maybe_pickle(data_folders,min_num_images_per_class,force=False):
    dataset_names = []
    for folder in data_folders:
        set_filename = folder + '.pickle'
        dataset_names.append(set_filename)
        if os.path.exists(set_filename) and not force:
            print('%s already present - Skipping pickling.' % set_filename)
        else:
            print('Pickling %s.',set_filename)
            
            
