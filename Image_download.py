from bing_image_downloader import downloader
downloader.download('2010 Toyota Camry exterior', limit=150,  output_dir='camry exterior', 
adult_filter_off=True, force_replace=False, timeout=60)