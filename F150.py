from bing_image_downloader import downloader
downloader.download('Ford F150 Exterior', limit=150,  output_dir='Ford Exterior', 
adult_filter_off=True, force_replace=False, timeout=60)