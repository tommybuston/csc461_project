from bing_image_downloader import downloader
downloader.download('2012 Honda Civic', limit=100,  output_dir='Civic', 
adult_filter_off=True, force_replace=False, timeout=60)