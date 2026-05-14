import turtle
import math
import time  # <-- 1. استيراد مكتبة الوقت للتحكم في السرعة
import random
# --- إعداد الشاشة والنافذة ---
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Heart for Halolty")

# --- هذه هي الخدمة لجعل النافذة فوق كل البرامج ---
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.attributes('-topmost', True)
# ----------------------------------------------------

# --- إعداد القلم (السلحفاة) ---
pen = turtle.Turtle()
pen.speed(0)  # أقصى سرعة
pen.color("hotpink") # لون بينك فاتح
pen.pensize(1)

# إيقاف التحديث التلقائي للشاشة لجعل الأنيميشن سلساً
screen.tracer(0, 0)

# --- كتابة الاسم "Hala" ---
pen.penup()
pen.goto(-380, 350) # الذهاب للزاوية العلوية اليسرى
pen.pendown()
pen.write("Hala", font=("Arial", 36, "bold"))
pen.penup()

# --- بدء أنيميشن التعبئة بالخطوط ---
# تحديد مركز القلب
center_x = 0
center_y = 0
# عدد الخطوط التي ستُرسم لملء القلب
num_lines = 1500

# رسم القلب عن طريق رسم خطوط من المركز إلى الخارج
for i in range(num_lines):
    # اختيار زاوية عشوائية
    t = random.uniform(0, 2 * math.pi)
    
    # حساب نقطة على محيط القلب بناءً على الزاوية العشوائية
    hx = 16 * math.sin(t) ** 3
    hy = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    
    # تكبير حجم القلب
    scale = 18
    hx *= scale
    hy *= scale
    
    # الانتقال إلى المركز
    pen.goto(center_x, center_y)
    pen.pendown()
    
    # رسم الخط إلى نقطة على محيط القلب
    pen.goto(hx, hy)
    pen.penup()
    
    # تحديث الشاشة بعد رسم كل خط لجعل الأنيميشن بطيئاً وواضحاً
    screen.update()
    
    # <-- 2. إضافة تأخير صغير جداً هنا -->
    # كلما زاد الرقم، أصبح الأنيميشن أبطأ
    time.sleep(0.005) 

# إخفاء السهم
pen.hideturtle()

# إبقاء النافذة مفتوحة
turtle.done()