# # s = """ f=0;seq=0;
# # HTTP/1.1 302 Moved Temporarily
# # Content-Type: text/html; charset=UTF-8
# # Location: http://www.aut.ac.ir/aut/fa/
# # Vary: Accept-Encoding
# # Server: AUT
# # Date: Sun, 08 Jul 2018 08:38:09 GMT
# # Content-Length: 0
# # """.encode()
# # print(s.decode())
# # s1 = "alireza hastam az behshahr".encode()
# # contolline = s.splitlines()[0]
# # contolline = contolline.decode()
# # contolbits = contolline.split(";")
# # f = contolbits[0].split("=")[1]
# # seq = contolbits[1].split("=")[1]
# # num = int(seq)
# # ack = "seq="+str(num+1)
# # print(ack)
# # # snew = []
# # # n = False
# # # h = "\r\n".encode()
# # # print(s.splitlines())
# # # for line in s.splitlines():
# # #     if n :
# # #         snew.append(line+h)
# # #     n = True
# # # data = bytearray().join(snew)
# # # print(data.decode())
# import re
import math

st = """HTTP/1.1 200 OK
Cache-Control: private
Content-Type: text/html; charset=utf-8
Vary: Accept-Encoding
Server: AUT
Date: Wed, 11 Jul 2018 08:50:45 GMT
Content-Length: 20885



<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Amirkabir University of Technology - Tehran Polytechnic</title>
<link rel="shortcut icon" href="images/favicon.ico"/>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta content="Amirkabir, University, Technology, Tehran, Polytechnic" name="keywords"/>
<link rel="stylesheet" href="layout/styles/layout.css" type="text/css" />
<script type="text/javascript" src="layout/scripts/jquery.min.js"></script>
<script type="text/javascript" src="layout/scripts/jquery.slidepanel.setup.js"></script>
<script type="text/javascript" src="layout/scripts/jquery.ui.min.js"></script>
<script type="text/javascript" src="layout/scripts/jquery.tabs.setup.js"></script>

<script type="text/javascript">
        function OnMouseIn (elem) {
                a.className="";
            elem.className = "active";

        }
        function OnMouseOut (elem) {
            elem.className = "";
            a.className="active";

        }
        function Init () {
            a.className="active";
        }

    </script>

</head>
<body onload="Init ()">

<!-- ####################################################################################################### -->
<div class="wrapper col1">
  <div id="header">
    <div id="logo">
      <img src="images/title-fa.png" alt="" />
    </div>
    <div class="fl_right">
      <img src="images/mission_1_3.png" alt="" />
    </div>
    <br class="clear" />
  </div>
</div>
<!-- ####################################################################################################### -->
<div class="wrapper col2">
  <div id="topnav">
    <ul>
      <li onmouseover="OnMouseIn (this)" onmouseout="OnMouseOut (this)">
          <a href="http://aut.ac.ir/aut/fa/">صفحه اصلی</a>
        <ul>
          <li class="last"><a href="http://aut.ac.ir/www/aut/main/?f=p0&s=departments&l=3">دانشکده ها و مراکز آموزشی</a></li>
                  <li><a href="http://virtualtour.aut.ac.ir">تور مجازی دانشگاه</a></li>
          <li><a href="#">آلبوم عکس</a></li>
          <li><a href="http://service.aut.ac.ir/">پرسش های متداول</a></li>
        </ul>
      </li>
      <li id="a" onmouseover="OnMouseIn (this)" onmouseout="OnMouseOut (this)"><a href="#">سرویسهای اعضاء</a>
      <ul>
          <li class="last"><a href="http://aut.ac.ir/www/aut/main/?l=3&s=page&p=portal">پورتال دانشگاه</a></li>
          <li><a href="http://aut.ac.ir/www/aut/main/?l=3&s=page&p=chargoon">اتوماسیون اداری</a></li>
          <li><a href="http://emd.aut.ac.ir/applications/Tracking/websitequery.aspx?SoftwareGuid=7C48F1EE-18C0-4406-84B0-3AD426CE5AEE&tableKey=1">پیگیری نامه</a></li>
          <li><a href="http://library.aut.ac.ir">کتابخانه</a></li>
          <li><a href="http://samad.aut.ac.ir/">پورتال تغذیه</a></li>
          <li><a href="http://service.aut.ac.ir/">سرویسها</a></li>
          <li><a href="http://Support.aut.ac.ir">سامانه پشتیبانی سرویس</a></li>
          <li><a href="http://aut.ac.ir/www/aut/main/?l=3&s=page&p=virtual">سیستم آموزش الکترونیکی</a></li>
          <li><a href="http://www.aut.ac.ir/aut/fa/AtoZ.aspx?g=1">فهرست وبگاهها</a></li>

        </ul>
      </li>
      <li onmouseover="OnMouseIn (this)" onmouseout="OnMouseOut (this)"><a href="#">پست الکترونیکی</a>
      <ul>
          <li class="last"><a href="https://webmail.aut.ac.ir">پست الکترونیکی</a></li>
          <li><font face="Tahoma"><a href="https://sepehr.aut.ac.ir/cic/admin/?f=p1&s=ad.pw.change&l=1">تغییر کلمه عبور</a></font></li>
          <li><a href="https://sepehr.aut.ac.ir/cic/admin/?f=p1&s=ad.pw&l=1">فراموشی کلمه عبور</a></li>
          <li><a href="https://sepehr.aut.ac.ir/cic/admin/?f=p1&s=ad.add&l=1">دریافت نام کاربری</a></li>

        </ul>
      </li>

      <li class="last" onmouseover="OnMouseIn (this)" onmouseout="OnMouseOut (this)"><a href="#">اطلاع رسانی</a>
       <ul>
          <li class="last"><a href="News.aspx">اخبار</a></li>
          <li><a href="http://www.aut.ac.ir/www/aut/main/?f=p0&s=ev.search&l=3&_p_st=1">رویدادها</a></li>
          <li><a href="#">اطلاعیه ها</a></li>

        </ul>
      </li>

       <li class="last" onmouseover="OnMouseIn (this)" onmouseout="OnMouseOut (this)"><a href="#">فارغ التحصیلان</a>
       <ul>
          <li class="last"><a href="http://edu.aut.ac.ir/iCMS/au/?f=p1&s=an.search&l=1&_p_st=1">اطلاعیه ها</a></li>
          <li><a href="http://edu.aut.ac.ir/iCMS/au/?f=p1&s=rg.search&l=1&_p_st=1">آیین نامه ها</a></li>
          <li><a href="http://edu.aut.ac.ir/iCMS/au/?f=p1&s=fm.search&l=1&_p_st=1">فرم ها</a></li>
          <li><a href="http://edu.aut.ac.ir/iCMS/au/?f=p1&s=fq.search&l=1&_p_st=1">پرسش های متداول</a></li>
          <li><a href="http://edu.aut.ac.ir/iCMS/au/?f=p1&s=an.view&id=3&l=1">دانشنامه های صادره</a></li>
          <li><a href="http://al.aut.ac.ir">اسامی فارغ التحصیلان</a></li>
        </ul>
      </li>
<li onmouseover="OnMouseIn (this)" onmouseout="OnMouseOut (this)"><a href="http://nikookaran.aut.ac.ir">خیرین حامی دانشگاه</a>
      <li onmouseover="OnMouseIn (this)" onmouseout="OnMouseOut (this)"><a href="#">ارتباط با ما</a>
      <ul>
          <li class="last"><a href="http://aut.ac.ir/www/aut/main/?f=p1&s=nw&l=3&id=1544">فرصتهای همکاری</a></li>
          <li><a href="http://phone.aut.ac.ir/">دفتر راهنمای تلفن</a></li>
          <li><a href="http://www.aut.ac.ir/www/aut/main/?f=p0&s=contact&l=3">تماسها</a></li>
        </ul>
      </li>

<li class="last" onmouseover="OnMouseIn (this)" onmouseout="OnMouseOut (this)"><a href="http://aut.ac.ir/aut/">[English]</a>

      </li>
    </ul>
  </div>
</div>
<!-- ####################################################################################################### -->

<div class="wrapper col3">
  <div id="featured_slide">
    <div id="featured_wrap">
      <ul id="featured_tabs">
<li><a href="#fc6">کسب رتبه اول دانشگاه امیرکبیر</a></li>
<li><a href="#fc2">دوره های آموزشی تابستان 97</a></li>

<li><a href="#fc3">مسابقات ملی هوافضا</a></li>
<li><a href="#fc1">سمینار بین المللی</a></li>
<li><a href="#fc4">سومین همایش سالانه رئولوژی</a></li>
          <li class="last"><a href="#fc5">حمایت از کالای ایرانی</a></li>

      </ul>
<div class="featured_box" id="fc6"><a href="http://aut.ac.ir/email/tir/970413p.pdf"><img src="../upload/SL/PT/173.gif" alt="" /></a>
          <div class="floater"><font face="Tahoma"><a href="http://aut.ac.ir/email/tir/970413p.pdf">« بیشتر بخوانید</a></font></div>
        </div>
<div class="featured_box" id="fc2"><a href="https://evand.com/aut"><img src="../upload/SL/PT/172.jpg" alt="" /></a>
          <div class="floater"><font face="Tahoma"><a href="https://evand.com/aut">« بیشتر بخوانید</a></font></div>
        </div>

<div class="featured_box" id="fc3"><a href="http://Aerocomp.ir"><img src="../upload/SL/PT/168.jpg" alt="" /></a>
          <div class="floater"><font face="Tahoma"><a href="http://Aerocomp.ir">« بیشتر بخوانید</a></font></div>
        </div>
<div class="featured_box" id="fc1"><a href="http://ispst.ir/"><img src="../upload/SL/PT/167.jpg" alt="" /></a>
          <div class="floater"><font face="Tahoma"><a href="http://ispst.ir/">« بیشتر بخوانید</a></font></div>
        </div>
 <div class="featured_box" id="fc4"><a href="http://ir-sor.com/"><img src="../upload/SL/PT/166.jpg" alt="" /></a>
          <div class="floater"><font face="Tahoma"><a href="http://ir-sor.com/">« بیشتر بخوانید</a></font></div>
        </div>
         <div class="featured_box" id="fc5"><a href="../upload/SL/PT/165.jpg"><img src="../upload/SL/PT/165.jpg" alt="" /></a>
          <div class="floater"><font face="Tahoma"><a href="../upload/SL/PT/165.jpg">« بیشتر بخوانید</a></font></div>
        </div>

      </div>
    </div>
  </div>
</div>

<!-- ####################################################################################################### -->
<div class="wrapper col4">
  <div id="homecontent">
    <div class="fl_left">
      <div class="column2">
        <ul>
          <li>
            <h2><font face="Tahoma"><a href="http://aut.ac.ir/www/aut/main/?f=p0&s=about&l=3">دانشگاه</a></font></h2>
             <ul>
                    <li><font face="Tahoma"><a href="http://aut.ac.ir/www/aut/main/?l=3&s=page&p=dean"> ریاست دانشگاه «</a></font></li>
                    <li><font face="Tahoma"><a href="http://faculty.aut.ac.ir/"> اعضای هیأت علمی «</a></font></li>
                    <li><font face="Tahoma"><a href="http://journals.aut.ac.ir/"> نشریات علمی - پژوهشی «</a></font></li>
                    <li><font face="Tahoma"><a href="http://publication.aut.ac.ir/"> انتشارات دانشگاه «</a></font></li>
                    <li><font face="Tahoma"><a href="https://www.aut.ac.ir/aut/fa/eng"> سلسله نشست بازمهندسی  «</a></font></li>
             </ul>
          </li>
          <li>
            <h2><font face="Tahoma">معاونت ها</font></h2>
             <ul>
                    <li><font face="Tahoma"><a href="http://edu.aut.ac.ir/iCMS/ed/"> آموزش و تحصيلات تکميلی «</a></font></li>
                    <li><font face="Tahoma"><a href="http://research.aut.ac.ir/"> پژوهش و فناوری «</a></font></li>
                    <li><font face="Tahoma"><a href="http://student.aut.ac.ir/"> فرهنگی و دانشجويي «</a></font></li>
                    <li><font face="Tahoma"><a href="http://admfin.aut.ac.ir/"> توسعه و مدیریت منابع «</a></font></li>
                    <li><font face="Tahoma"><a href="http://campus.aut.ac.ir/vi"> امور بین الملل «</a></font></li>

             </ul>
          </li>

        <li>
            <h2>آموزش</h2>
              <ul>
                    <li><font face="Tahoma"><a href="http://aut.ac.ir/www/aut/main/?f=p0&s=departments&l=3"> دانشکده ها و مراکز آموزشی «</a></font></li>
                    <li><font face="Tahoma"><a href="Calendar.aspx"> تقويم آموزشی «</a></font></li>
                        <li><font face="Tahoma"><a href="http://edu.aut.ac.ir/iCMS/pg/?f=p1&s=an.search&l=1&_p_st=1"> تحصيلات تکميلی «</a></font></li>
                    <li><font face="Tahoma"><a href="http://aut.ac.ir/aut/fa/edu.aspx"><font color="052161"><b> برنامه‌های جدید آموزشی «</b></font></a></font></li>
                <li><font face="Tahoma"><a href="http://edu.aut.ac.ir/iCMS/et/">استعدادهای درخشان و المپیادها «</a></font></li>

             </ul>

          </li>
                <li>
           <h2>امور سازمانی</h2>
             <ul>
                    <li><font face="Tahoma"><a href="http://edari.aut.ac.ir"> امور اداری و پشتیبانی «</a></font></li>
                    <li><font face="Tahoma"><a href="http://aut.ac.ir/jazb"> جذب هیأت علمی «</a></font></li>
                    <li><font face="Tahoma"><a href="http://al.aut.ac.ir/"> فارغ التحصيلان «</a></font></li>
                    <li><font face="Tahoma"><a href="http://pr.aut.ac.ir"> روابط عمومی «</a></font></li>
                    <li><font face="Tahoma"><a href="http://alumni.aut.ac.ir"> جامعه فارغ التحصیلان «</a></font></li>
             </ul>
          </li>

        </ul>
        <br class="clear" />
      </div>
      <div class="column3">
        <h2><a href="http://www.aut.ac.ir/www/aut/main/?f=p0&s=mi.search&_p_st=1">خبرنامه و تازه های نشر دانشگاه صنعتی امیرکبیر</a></h2>
          <div class="fl_leftIMG"><a href="http://www.aut.ac.ir/www/aut/main/?f=p0&s=mi.search&_p_st=1"><img id="Image1" src="../upload/NL/PT/37.jpg" border="0" /></a></div>
<iframe src="frame/autoPlayFade/index.html" width="205px" height="255px" frameborder="0"
                        scrolling="no"></iframe>
      </div>
    </div>

    <div class="fl_right">
         <div class="fl_announce">
         <h2>اطلاعیه ها ... <a href="Announce.aspx"><font color="052161"><small>سایر اطلاعیه ها</small></font></a></h2>
      <ul>
 <li>» <a href="http://edu.aut.ac.ir/iCMS/eu/?f=p1&s=an.view&id=28&l=1" target="_blank"> اطلاعیه ثبت نام ترم تابستان ۱۳۹۷ </a></li>
          <li>» <a href="http://edu.aut.ac.ir/iCMS/pe/?f=p1&s=an.view&id=78&l=1" target="_blank">شهریه سال 98-97 مقطع دکتری دوره نوبت دوم و پردیس خودگردان</a></li>
<li>» <a href="http://edu.aut.ac.ir/iCMS/pg/?f=p1&s=an.view&id=151&l=1">پذیرش دانشجوی دکترای سال ۹۸-۱۳۹۷</a></li>
          <li>» <a href="http://edu.aut.ac.ir/iCMS/sv/?f=p1&s=an.search&l=1&_p_st=1">ارزیابی دروس کارشناسی و تحصیلات تکمیلی نیمسال دوم 97-96</a></li>


          <li>» <a href="http://mmwatt.aut.ac.ir" target="_blank">پنجمین کنفرانس بین المللی فناوری موج میلیمتری و تراهرتز</a></li>



      </ul></div>
      <h2> اخبار دانشگاه ... <a href="News.aspx"><font color="052161"><small>سایر اخبار</small></font></a></h2>
      <ul>

        <li>
          <a href="NewsInfo.aspx?id=4828"><div class="imgholder"><img src="../upload/NS/SM/4828.jpg" alt="" /></div>
          <p><strong>توسعه همکاری‌ها با کارگاه‌های تخصصی</strong></p></a>
          <p>دانشگاه صنعتی امیرکبیر در راستای توسعه همکاری‌های علمی با اساتید خارجی در مهرماه سال جاری اقدام به برگزاری کارگاه‌های تخصصی در 9 حوزه علمی کرده است...
          </p>
        </li>

        <li>
          <a href="NewsInfo.aspx?id=4827"><div class="imgholder"><img src="../upload/NS/SM/4827.jpg" alt="" /></div>
          <p><strong>مسابقات آب شیرین کن‌های خورشیدی</strong></p></a>
          <p>دومین دوره مسابقات آب شیرین کن های خورشیدی با حضور تیم هایی از سراسر کشوردر سه بخش آب صنعتی ، آب شرب خانگی ZLD برگزار می شود...
          </p>
        </li>

        <li>
          <a href="NewsInfo.aspx?id=4826"><div class="imgholder"><img src="../upload/NS/SM/4826.jpg" alt="" /></div>
          <p><strong>رتبه اول ملی دانشگاه در رتبه بندی ISC </strong></p></a>
          <p>کسب رتبه یک دانشگاه صنعتی امیرکبیر در نظام رتبه بندی ISC در میان دانشگاه‌های صنعتی کشور در
1397 ...

          </p>
        </li>

        <li>
          <a href="NewsInfo.aspx?id=4825"><div class="imgholder"><img src="../upload/NS/SM/4825.jpg" alt="" /></div>
          <p><strong>تشخیص به هنگام بیماری‌های دریچه قلبی</strong></p></a>
          <p>روشی برای تشخیص به هنگام بیماری‌های دریچه قلبی از سوی محققان کشور ...
          </p>
        </li>

      </ul>



    </div>

    <br class="clear" />
  </div>
</div>
<!-- ####################################################################################################### -->
<div class="wrapper col5">
  <div id="footer">

    <div id="map">
      <h2><font face="Tahoma">نقشه راهنما</font></h2>
      <center><a href="https://www.google.com/maps/@35.7042441,51.4096136,19z" target="_blank"><img src="../images/map.jpg" alt="Google Map of Amirkabir University of Technology"/></a>
<br><a href="http://virtualtour.aut.ac.ir/">تور مجازی دانشگاه </a>
</center>

    </div>
    <div class="footbox">
      <h2><font face="Tahoma">دسترسی سریع</font></h2>
      <ul>
            <li><a href="http://omana.aut.ac.ir/">هیأت امناء «</a></li>
            <li><a href="http://aut.ac.ir/www/aut/main/?l=3&s=page&p=heatraees">هیأت رئیسه «</a></li>
            <li><a href="http://aut.ac.ir/jazb/">هیأت اجرایی جذب «</a></li>
            <li><a href="http://aut.ac.ir/www/aut/main/?l=3&s=page&p=shora">شورای دانشگاه «</a></li>
            <li><a href="http://aut.ac.ir/www/aut/main/?l=3&s=page&p=riasat">مدیرکل دفتر ریاست «</a></li>
            <li><a href="http://aut.ac.ir/www/aut/main/?l=3&s=page&p=nezarat">نظارت و ارزیابی «</a></li>
            <li><a href="http://www.aut.ac.ir/aut/fa/files/rahbordi.pdf">کتابچه سند راهبردی «</a></li>
            <li><a href="http://www.swf.ir/">صندوق رفاه دانشجویان وزارت علوم «</a></li>
            <li class="last"><a href="http://idea.aut.ac.ir/">سامانه جامع نظام پیشنهادها «</a></li>
      </ul>
    </div>
        <div class="footbox">
      <h2><font face="Tahoma">دسترسی سریع</font></h2>
      <ul>
        <li><a href="http://ideasbazaar.ir">ایده بازار «</a></li>
        <li><a href="http://research.aut.ac.ir/Office_Of_Enterepenership_And_Incubation/Default.aspx">اداره کل فناوری و توسعه نوآوری «</a></li>
        <li><a href="../Files/farhangi.pdf">سند چشم انداز فرهنگی «</a></li>
        <li><a href="http://aut.ac.ir/general/map.pdf">نقشه جامع علمی کشور «</a></li>
        <li><a href="http://aut.ac.ir/www/aut/main/?f=p0&s=page&l=3&p=download">پایگاه نرم افزار-دانلود «</a></li>
        <li><a href="http://aut.ac.ir/www/aut/main/?l=3&s=page&p=course"> معرفی رشته «</a></li>
        <li><a href="http://jdamirkabir.ac.ir/">جهاد دانشگاهی واحد امیرکبیر «</a></li>
        <li><a href="http://student.aut.ac.ir/images/manshor.pdf">منشور حقوق دانشجویی «</a></li>
        <li class="last"><a href="http://www.aut.ac.ir/aut/fa/olampiad/year.aspx">برگزيدگان المپيادي دانشگاه «</a></li>

      </ul>
    </div>
    <div class="footbox">
      <h2><font face="Tahoma">دسترسی سریع</font></h2>
      <ul>
<li><a href="http://www.aut.ac.ir/akumembers/">ویرایش صفحات اساتید «</a></li>
<li><a href="http://appraisal.aut.ac.ir/logon.aspx">ارزیابی کارکنان «</a></li>
            <li><a href="http://Support.aut.ac.ir">سامانه پشتیبانی سرویس «</a></li>
            <li><a href="http://karaway.aut.ac.ir">کارآموزی، کارورزی و کاریابی  «</a></li>
            <li><a href="http://sao.aut.ac.ir/sao/index.php?lang=fa">انجمن های علمی «</a></li>
            <li><a href="http://ieeesb.aut.ac.ir">IEEE شاخه دانشجویی «</a></li>
            <li><a href="http://www.msrt.ir">وزارت علوم، تحقیقات و فناوری «</a></li>
            <li><a href="http://bmn.ir/">بنیاد ملی نخبگان «</a></li>
            <li><a href="http://www.insf.org/">صندوق حمایت از پژوهشگران «</a></li>

            <li><a href="http://civil.aut.ac.ir/Default,fa-IR,Civil,Content,Document,Name,DBGEO,TabID,271.aspx">بانک اطلاعاتی داده های ژئوتکنیکی «</a></li>

      </ul>
    </div>


    <font face="Tahoma">
    <br class="clear" />
        </font>
  </div>
</div>
<!-- ####################################################################################################### -->
<div class="wrapper col6">
  <div id="copyright">
    <p align="right"><img src="../images/aut_text_s_1.png" alt=""/> © حق نشر دانشگاه صنعتی امیرکبیر.</p>
    <p>دانشگاه مسئول محتوای دیگر پایگاه ها نیست.
۴۲۴ خیابان حافظ، تهران، ایران.
صندوق پستی ۴۴۱۳-۱۵۸۷۵. ۶۴۵۴۰ (۲۱) ۹۸+ </p><p>کد پستی 1591634311.</p>

  </div>
</div>
</body>
</html>
"""
# start = st.index("<!DOCTYPE html")
# end   = st.index("</html>")
# st[start:end+len("</html>")]

# f = 1
# seq = 21
# alireza = ("f="+str(f)+";seq="+str(seq)+";\r\n").encode()
# print(len(alireza))
# dataproxy = ("""f=0;seq=0;
# dewrgethynrgdfsd
# werwetnjrytmuj
# dwferngdmfh
# """).encode()
# print("data proxy",(dataproxy).decode())
# datatmp = '\n'.join(str(dataproxy.decode()).split('\n')[1:])
# print("datatmp", datatmp)
# tmp = []
# data = st
# i = 0
# n = math.ceil(len(data)/500)
# for i in range (0,n):
#     if i == n - 1 and n != 1 :
#         tmp.append(data[i*500:-1].encode())
#     else:
#         tmp.append(data[i * 500:(i + 1) * 500 - 1].encode())
# print("*********************************************",(bytearray().join(tmp)).decode())
# def carry_around_add(a, b):
#     c = a + b
#     return (c & 0xffff) + (c >> 16)
#
# def checksum(msg):
#     s = 0
#     for i in range(0, len(msg)-1, 2):
#         w = ord(msg[i]) + (ord(msg[i+1]) << 8)
#         s = carry_around_add(s, w)
#     return ~s & 0xffff
#
# message1 = "salam azizam khoobi kheili khari"
# # print(checksum(message1))
#
# message2 = "aslam azizam khoobi kheili khari"
# # print(checksum(message2))
#
# message3 = "aalam azizam khoobi kheili khari"
# # print(checksum(message3))
#
# frag = b'f=2;seq=42;\r\n\xd9\xbe\xd8\xb3\xd8\xaa\xdb\x8c 1591634311.</p>\r\n  \r\n  </div>\r\n</div>\r\n</body>\r\n</html>'
# print(checksum(str(frag)))
import hashlib
hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())