from bing_image_downloader import downloader
downloader.download('2007 Subaru Tribeca', limit=100,  output_dir='Tribeca', 
adult_filter_off=True, force_replace=False, timeout=60)