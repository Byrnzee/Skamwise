from django.forms import ModelForm
from .models import URLWarning, URLSafe
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class WarningBlock(ModelForm):
    class Meta:
        model = URLWarning
        fields = '__all__'

class SafeBlock(ModelForm):
    class Meta:
        model = URLSafe
        fields = '__all__'