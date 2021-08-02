from utils import img_html

linkedin = img_html('media/logo-linkedin.png', 'max-width:32px', '')
github = img_html('media/logo-github.png', 'max-width:32px', '')
facebook = img_html('media/logo-fb.png', 'max-width:32px', '')
email = img_html('media/logo-email.png', 'max-width:32px', '')

socia_media_links = f"""
    <div style='text-align:center;'>
        <div style='inline-block'>
        <a href='mailto:tomdugma@gmail.com' style='margin-right:5px'>{email}</a>
        <a href="https://www.linkedin.com/in/tom-dugma-b2aa521b3/" target= '_blank' style='margin:5px'>{linkedin}</a>
        <a href="https://github.com/tomdugma" target= '_blank' style='margin:5px'>{github}</a>
        <a href="https://www.facebook.com/tom.dugma/" target='_blank' style='margin:5px'>{facebook}</a>
        </div>
    </div>
    """