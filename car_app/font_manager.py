"""
مدير الخطوط العربية - يدعم تحميل الخطوط على جميع الأنظمة
"""
import os
from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONTS_DIR = Path(__file__).parent.parent / 'static' / 'fonts'

def get_system_font_path():
    """الحصول على مسار خط عربي من النظام"""
    # مسارات محتملة للخطوط العربية على أنظمة مختلفة
    # نبحث عن خطوط تدعم العربية: DejaVuSans, Noto, Liberation
    possible_paths = [
        # Linux - خطوط عربية
        '/usr/share/fonts/truetype/noto/NotoSansArabic-Regular.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
        # Windows - خطوط عربية
        'C:\\Windows\\Fonts\\arial.ttf',  # Arial يدعم العربية على Windows
        'C:\\Windows\\Fonts\\calibri.ttf',
        'C:\\Windows\\Fonts\\times.ttf',
        'C:\\Windows\\Fonts\\DejaVuSans.ttf',
    ]
    
    for path in possible_paths:
        if Path(path).exists():
            print(f"✓ وجدت الخط: {path}")
            return path
    return None

def register_arabic_fonts():
    """تسجيل خطوط عربية للاستخدام في PDF"""
    try:
        # محاولة 1: البحث عن خط عربي على النظام
        system_font = get_system_font_path()
        if system_font:
            try:
                pdfmetrics.registerFont(TTFont('ArabicFont', system_font))
                pdfmetrics.registerFont(TTFont('ArabicFontBold', system_font))
                print(f"✓ تم تسجيل الخط: {system_font}")
                return True
            except Exception as e:
                print(f"تحذير: لم يتمكن من تسجيل {system_font}: {e}")
        
        # محاولة 2: استخدام Courier كبديل افتراضي (يدعم Unicode)
        try:
            pdfmetrics.registerFont(TTFont('ArabicFont', 'Courier'))
            pdfmetrics.registerFont(TTFont('ArabicFontBold', 'Courier-Bold'))
            print("✓ تم تسجيل Courier كخط عربي بديل")
        except:
            print("تحذير: لم يتمكن من تسجيل أي خط عربي، سيتم استخدام الخطوط الافتراضية")
            
        return False
        
    except Exception as e:
        print(f"خطأ في تسجيل الخطوط: {e}")
        return False

def get_arabic_font_name():
    """الحصول على اسم الخط العربي المسجل"""
    try:
        # تحقق من ما إذا كان الخط موجود
        available_fonts = pdfmetrics.tt2ps._fonts if hasattr(pdfmetrics.tt2ps, '_fonts') else {}
        
        if 'ArabicFont' in available_fonts:
            return 'ArabicFont'
        if 'ArabicFontBold' in available_fonts:
            return 'ArabicFontBold'
        if 'Courier' in available_fonts:
            return 'Courier'
    except:
        pass
    
    # إذا لم يوجد، استخدم Helvetica كبديل
    return 'Helvetica'

def get_arabic_font_bold():
    """الحصول على اسم الخط العربي الغامق"""
    try:
        available_fonts = pdfmetrics.tt2ps._fonts if hasattr(pdfmetrics.tt2ps, '_fonts') else {}
        
        if 'ArabicFontBold' in available_fonts:
            return 'ArabicFontBold'
        if 'Courier-Bold' in available_fonts:
            return 'Courier-Bold'
    except:
        pass
    return 'Helvetica-Bold'

