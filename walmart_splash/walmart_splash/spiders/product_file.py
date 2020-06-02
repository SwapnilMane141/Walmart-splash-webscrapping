# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import json


class ProductFileSpider(scrapy.Spider):
    name = 'product_file'
    allowed_domains = ['grocery.walmart.com']
    start_urls = ['https://grocery.walmart.com/signin']

    # a=input("Enter the pincode = ")

    script=''' 
   function main(splash, args)
        splash.private_mode_enabled=false
        headers = {['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36", ['cookie'] ="vtc=bAEUwpgBVEeZnJTIALKD3M; _gcl_au=1.1.962060150.1591075214; viq=Walmart; TBV=7; _abck=iftied5m0ycpyuvf648l_1899; _pxvid=be2445b4-a490-11ea-b986-0242ac120009; s_vi=[CS]v1|2F6AF0C80515AEF7-4000063C00CE2825[CE]; WMP=4; oneapp_customer=true; ONEAPP_CUSTOMER=true; __gads=ID=ce08421213903999:T=1591075222:S=ALNI_MbMPRbx0EVcYNgq2QhsIJscegqevw; bstc=YQWw1jylyXGyalgIH0Vg9I; TS01af768b=01538efd7cac5c2b2820f62d281f53e72be355ca158caac62324a614d4cb34bc47a45da3e590c9009e3656a14cd3a74dc3ff5ee978; TS012c809b=01538efd7cac5c2b2820f62d281f53e72be355ca158caac62324a614d4cb34bc47a45da3e590c9009e3656a14cd3a74dc3ff5ee978; TB_DNS_Perf_Test=1; TB_DC_Dist_Test=1; TB_DC_Flap_Test=1; mobileweb=0; ty-fe-env=n-blue; cart-fe-env=n-blue; xo-fe-env=n-blue; pac-fe-env=n-blue; thPillsWeb=true; go-xpa=6Ohhx|8ftLP|BnGdF|Bxmol|G3Z6T|GqhsP|Hhsz3|OSz3t|Spqwp|UL0-e|Uhvy5|UvvRW|Wt19z|YCiRs|aDi4V|lyrHR|qacLZ|vINoo|wW3CL|zOzKh; go-exp-ck=6Ohhx18ftLP1Bxmol1G3Z6T2GqhsP1Hhsz31UL0-e1Uhvy51Wt19z1lyrHR2; GCRT=abbb6f3d-b45a-41f8-8b1e-d7724196e848; hasGCRT=1; wm_mystore=Fe26.2**43e65177ae9db608dc5b3a379e6bcf5988c37775e10527cc7a85e87511c348aa*CNwfRlJukFcwGlLVrQDG4g*FKALoFcVfLDeudYygAy1olm_rEzT-J9DvqFPs4l76ZBb2aJ-edKE2gJ4Aw5F1vuMguUpLt1NoU6-n2yoMDqYV1AWqVs8bKnkNkOYGjJ-TTEF9PP7xEj1X0PLd_L4Ep9pYVOZYawA457175meFZ8W7A**7f4b8d40d9a80eb645085c3c8aa967ff3d3f2214482dfe4172d68d63e3130158*Qh1pQg5xdEuFDFLYVVUwvC_Aod-QKnq0Swr8bXBaOqk; ACID=e5d89dd0-a4a1-11ea-9339-4dc8ebf0885b; hasACID=1; TS01e1b9cb=01c5a4e2f9e4ac8d4f8fce7a54553d14a49cf751972daa97e87eebd212ff59893a65e2f548508f12608453a5b0f5f121bf9f0f8a9f; TS01624fdb=01c5a4e2f9e4ac8d4f8fce7a54553d14a49cf751972daa97e87eebd212ff59893a65e2f548508f12608453a5b0f5f121bf9f0f8a9f; xpa=6Ohhx|8ftLP|BnGdF|Bxmol|G3Z6T|GqhsP|Hhsz3|OSz3t|Spqwp|UL0-e|Uhvy5|UvvRW|Wt19z|YCiRs|aDi4V|lyrHR|qacLZ|vINoo|wW3CL|zOzKh; xpm=0%2B1591082587%2BbAEUwpgBVEeZnJTIALKD3M~%2B0; exp-ck=6Ohhx18ftLP1Bxmol1G3Z6T2GqhsP1Hhsz31UL0-e1Uhvy51Wt19z1lyrHR2; go-xpm=0%2B1591082587%2BbAEUwpgBVEeZnJTIALKD3M~%2B0; go-ty-fe-env=n-blue; go-cart-fe-env=n-blue; go-xo-fe-env=n-blue; go-pac-fe-env=n-blue; go-thPillsWeb=true; TS01e3f36f=0130aff232eedc8ae73a3742d5b0610b03d3fad7f149dabd777125a7d215602ae110d35c2b5a287f8e7eb79bffa13a8090c30dc65a; TS018dc926=0130aff232eedc8ae73a3742d5b0610b03d3fad7f149dabd777125a7d215602ae110d35c2b5a287f8e7eb79bffa13a8090c30dc65a; _pxff_rf=1; _pxff_fp=1; _px3=268292b329d6a76a0fc03d1077b152bff296e3a6d7a2955b35db7bcdf85a20ca:9pe8ymbzhaS5DRSAs49Vr2lA6rONbgTmWwZxdVPEI/A+2Og0pSMnTWppRiBklWtzmHlwd+ScI+ALNx149LPzEw==:1000:bH76pKzEZ5CHKJb4Ft+a9fejki1KAUcjnmtE1ATfyopVw/BjKrXzlZTRYmhpAq+3N5rFeWkDhWCid5jsxdEVLUjeG9mBF7zRlALQBqGaxWQEWvh87ZvrV8lwakGH62t8KdQa0EOphFg32JpkaLGLuAlT6H5xmUZe/Q0epGfm5yk=; TS011baee6=0130aff2322e29da49aa84fb98ed86746baa60ef4925fbede14e427b6b4fb684db20ac6f0b75ba6698347058327e7abf20f90190f9; s_sess=%20ent%3Dnt_SignIn%257CON_AUTH_SUCCESS%3B%20s_cc%3Dtrue%3B%20chan%3Dorg%3B%20v54%3DAccount_SignIn%257CON_AUTH_SUCCESS%3B%20cps%3D0%3B%20s_sq%3D%3B%20v59%3D%3B; akavpau_p0=1591083196~id=64cf3739b01d029fbabddc5da55c97ab; _pxde=d4db3c087dd614558a12afe4843907878ef4cf0c9ecd3203c3ddcec5e652d318:eyJ0aW1lc3RhbXAiOjE1OTEwODI2MDA4OTAsImZfa2IiOjAsImlwY19pZCI6W119; s_pers=%20s_fid%3D5CB36F62FC5468A4-052F0C9BE69B3706%7C1654154600941%3B%20s_v%3DY%7C1591084400946%3B%20gpv_p11%3DSign%2520In%7C1591084400971%3B%20gpv_p44%3Dno%2520value%7C1591084400977%3B%20s_vs%3D1%7C1591084400984%3B",['content-type'] = "application/json"}
        splash:set_custom_headers(headers)
        assert(splash:go(args.url))
        assert(splash:wait(0.5))
        
        email_box=assert(splash:select("div input#email"))
        pass_box=assert(splash:select("div input#password"))
        email_box:mouse_click()
        email_box:send_text("testsplash141@gmail.com")
        pass_box:mouse_click()
        pass_box:send_text("testsplash141")
        pass_box:send_keys("<Enter>")
        assert(splash:wait(8))
        
        change_but=assert(splash:select("button.button-link.FulfillmentBanner__btn___3av1F"))
        change_but:mouse_click()
        assert(splash:wait(1))
        
        pincode_box=assert(splash:select("input[aria-label='Search For locations via Zip Code:']"))
        assert(splash:wait(0.5))
        pincode_box:mouse_click()
        pincode_box:send_keys("<Backspace>")
        pincode_box:send_keys("<Backspace>")
        pincode_box:send_keys("<Backspace>")
        pincode_box:send_keys("<Backspace>")
        pincode_box:send_keys("<Backspace>")
        pincode_box:send_text("90660")
        pincode_box:send_keys("<Enter>")
        assert(splash:wait(3))
        walmart_store=assert(splash:select("li.List__tile___108pZ"))
        walmart_store:mouse_click()
        assert(splash:wait(1))
        continue_but=assert(splash:select("button.button-block.button-primary"))
        continue_but:mouse_click()
        assert(splash:wait(1))
        change_but=assert(splash:select("button[aria-label='Change']"))
        assert(splash:wait(1))
        change_but:mouse_click()
        assert(splash:wait(2.5))
        close_but=assert(splash:select("a.button-primary"))
        close_but:mouse_click() 
        
        return splash:html()
    end
    '''

    def start_requests(self):
        yield SplashRequest(url='https://grocery.walmart.com/signin',callback=self.parse,endpoint='execute',args={
            'lua_source':self.script
        })
    
    def parse(self, response):

        query=  {
                "cartItems":[
                    {
                        "offerId":"51CDBC4374C0490BAAD9C9214126D179",
                        "quantity":1
                    }
                ]
                }
        item=response.xpath("//a[@data-automation-id='accountLink']")
        if item:
            print("successfully reached the walmart page")
        else:
            print("Try again and dont forget to change the pincode")
        
        yield scrapy.Request(url='https://grocery.walmart.com/v3/api/cart/91a97db0-5b80-49f1-9c8c-bfeb2dc1d721/items',
                    callback=self.final,method='PUT',body=json.dumps(query),headers={
                        'content-type':'application/json',
                        'cookie':'vtc=bAEUwpgBVEeZnJTIALKD3M; _gcl_au=1.1.962060150.1591075214; viq=Walmart; s_vi=[CS]v1|2F6AF0C80515AEF7-4000063C00CE2825[CE]; WMP=4; oneapp_customer=true; ONEAPP_CUSTOMER=true; __gads=ID=ce08421213903999:T=1591075222:S=ALNI_MbMPRbx0EVcYNgq2QhsIJscegqevw; bstc=T0RqP4uEm-w2u-O__j7a6E; TS01af768b=01538efd7c7a1d94d73429d4ba874e4e78c3eefe2d2ea409b0390b42ca6f4bc41a339bbe42fc1582ff632734cf81750017c4e49135; TS012c809b=01538efd7c7a1d94d73429d4ba874e4e78c3eefe2d2ea409b0390b42ca6f4bc41a339bbe42fc1582ff632734cf81750017c4e49135; __cfduid=df9c096ed2029c08e1782be8adf425b841591113284; hasGCRT=1; TB_DNS_Perf_Test=1; TB_DC_Dist_Test=1; TB_DC_Flap_Test=1; mobileweb=0; ty-fe-env=n-blue; cart-fe-env=n-blue; xo-fe-env=n-blue; pac-fe-env=n-blue; thPillsWeb=true; go-xpa=6Ohhx|8ftLP|BnGdF|Bxmol|G3Z6T|GqhsP|Hhsz3|OSz3t|Spqwp|UL0-e|Uhvy5|UvvRW|Wt19z|YCiRs|aDi4V|lyrHR|qacLZ|vINoo|wW3CL|zOzKh; go-exp-ck=6Ohhx18ftLP1Bxmol1G3Z6T2GqhsP1Hhsz31UL0-e1Uhvy51Wt19z1lyrHR2; TS01e3f36f=01c5a4e2f9d9fba4d5a5575e3d26dca712181cb6ec736804bcfb621989e5dd8727da6ea790cdffd96421fd4fe8e11cc26f7e32aac9; TS018dc926=01c5a4e2f9d9fba4d5a5575e3d26dca712181cb6ec736804bcfb621989e5dd8727da6ea790cdffd96421fd4fe8e11cc26f7e32aac9; auth=MTAyOTYyMDE4gu55aMId3x29wCCYjTTIGchh%2FqWue5F%2FTH40SE1l2lLrgm3AcxBwBAWvp8XXvMWkH19XMyODM5%2FbdHRXvRwHh9oqqZ%2F%2FDd%2BnmLuczzUb3z%2BABuZPdeU1b5hhEBS%2BJVOlyc2e0wwmZvaRm87PQlkVaVWB4BkzDU4Jfl8GThDmYvIAlLd0nNOV%2BFT%2BuNYu7wKyb9O6gaVmm%2Bfx7A5ObCHtCz%2Bl3AeOul%2BzSsRNSF83bZcl462Il9IktR9z3xa%2FEqPEGq%2Bmp%2BP%2FcaxzgRYSMg3E7TUNgOjX3D2LEdNCTFD6j8JV1Y6qTjqXsJgmChnjomIzz36W9qqnXgI0gcFhoalnGpBU%2Fu8Rrlml5VhnQZP0GSC8aXYqmyXdeSmH%2FtVy74yg; rtoken=MDgyNTUyMDE4Vc%2B8HeO2TKveYBo1beyXtxeXirEIkjHqtFsmNCzXSNHzvLyX5dBgbHDeC8zI3XixY7%2BePgoMihDY7R%2BzguKdGAqdVMbQBhggVBLFYWTvx56oudDRc7ekLUDT%2BOCGtMbKpBLMYX2112v%2FeV2pBK2KC%2FmLRnMm6yfnLItv5k1m9jr9uwQqpt6hiFScKz71rNs1BjAwX4LlJLO8L6iEWgzcmR8ltylpjojGkQV%2FrqqV80e2g%2F7qL%2BC4I1tt5rTbjGRhftufOYqO5HN3l%2BkGsgAz%2BAcvSXCqN9hTAgj4G4WhJvUkPEz8J3PVfEeTROEC28irxVT%2BqJckj4UJ0UenkNRstBf7zlYnNMKFYxnnMKHCWciHK3NlQQyVN4fjcrttl1lyUJ5tzlnAwL%2F96aMLyJ5b9w%3D%3D; SPID=986146a6fd4bd5e165b63b6e929e6e13689ccb5de5d083559300d87b50f1bab2d674ff41a78478564655dc7d7116acd1myacc; CID=7fe2d60f-2356-44a0-b827-ac6e8e44db0c; hasCID=1; customer=%7B%22firstName%22%3A%22Test%22%2C%22lastNameInitial%22%3A%22S%22%2C%22rememberme%22%3Atrue%7D; type=REGISTERED; go-xpm=1%2B1591113453%2BbAEUwpgBVEeZnJTIALKD3M~%2B0; go-ty-fe-env=n-blue; go-cart-fe-env=n-blue; go-xo-fe-env=n-blue; go-pac-fe-env=n-blue; go-thPillsWeb=true; xpa=7Ivc1|UvvRW|onmki; exp-ck=onmki2; akavpau_gp2=1591114081~id=cbff64bc4bbae2aa2f8d3bed18e0158c; xpm=1%2B1591113481%2BbAEUwpgBVEeZnJTIALKD3M~7fe2d60f-2356-44a0-b827-ac6e8e44db0c%2B1; member=0; GCRT=91a97db0-5b80-49f1-9c8c-bfeb2dc1d721; TS01bae75b=01538efd7c4da1a64946f6e39755420411be989c1dc2d3aa8ec72909aaa7943136dd13bf469a52e813a00df0ffd45cb5a764e8b0c2; wm_mystore=Fe26.2**d9883848272eec81a33122c3488232be6e09829eca6bfaad57985f84a489f6af*BPJDjS5Os3Kv5J-lTHg6jA*-idvWpG_m7u_XaKrq-TNYyX6V4ZNXB8qtIqmG4g2JUM2Zlm10DdFUR5Ylu0FWtP0sANlI2HuxaVxjtMrZxsULJvajLSWwaEmB9Y0ukCp1SuC7iSPRyjVULmkd2SGZNWq4IW6zHOU0R2vTCrCUGAMe6bEYsjTYx4JQ5QS2dSHfQq1sCIRt6O2hYkUjncI4HvQOlnnhquOIveoAKw9frOseeEmPjJ5rR9AyBQ_hi-KJeCUn4ZidLpy01nZwnEu7T-qU9gGk1UD0I8XcEtjl8_ibYHXOrpJMbNxt6AYmuyPJCku6VmkD3GYwF6KyBJyR_WMC2VtNeNh69s483VJXZGnfQfnofz4WAUE4jdcCSE5z97LiR5iqGOly10eQ0iTtlvTaWyYWG4nvlV9lzN39Zs_O3cGHBiUnx_XaB8zL0Vu0nV1xYxE_08LhLD70EMiO6XpzDukYV7-mYE6xTFZJCZeNywDDOfugAvS8obuk9A3arQIwwN0ou0r4uCqeR-1FjQ4v2bApk1OnI2u_3eeMdNiEAAmx4vmz9b2bfv7uApae8BXXs3oEKFN4CzUYg5khZXO0-_3KcZ2G-6PYMOcAPRMib1um-4S1PQzWzT7IX2DJS6h0r5bI7CZ4qn2jfsQPYKFfMcrz0NWYtMoUMu4xN0BURPBoSSwrz24cur7fNjADKreb5xRyEBAEk7OUxLod0PxRCesfD9_pbOkAdJP0ZL6WmpJYmiNnfyAOCq-nDut1EM-5ZTP8I1PIYuoVL_4XGQgPeJcgVfYw98fjI4XKSIU0PT_tSpG9R0QRVa6WMrzbRCGCbGln2PQ3H_Fxfco8DzpZltKe5DGGiJ75k1teW8SLlSfhYkG5Rg2LY5p68Vq34k**249184e242f82983a3730fb4f5fe48c3fb9152e8ec48d88829dc376664ebf203*MaCinmTVMGOJembizisfmgOYVW39AsHTcSt8P8aaB_s; x-csrf-jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiY29va2llIiwidXVpZCI6IjA2N2NkYmQwLWE0ZWEtMTFlYS05NWU5LWZiMmQzMmE3ODUwOCIsImlhdCI6MTU5MTExMzU2MiwiZXhwIjoxNTkyMTkzNTYyfQ.Fi4ert4LsGII0fOA2vTNAPPp59p4W-UUtv26-ymI8wk; akavpau_gp4=1591114163~id=ad802f0639399cef3d15c2ad0daaac15; TS01f4281b=01c5a4e2f941955e2d3c2f9319868e94fdaf34f5816ecc1b9816c29baa6ed80d68513a59f30839d018300c7b3c1c175eaa87c17a7e; TS01e1b9cb=01c5a4e2f941955e2d3c2f9319868e94fdaf34f5816ecc1b9816c29baa6ed80d68513a59f30839d018300c7b3c1c175eaa87c17a7e; TS01624fdb=01c5a4e2f941955e2d3c2f9319868e94fdaf34f5816ecc1b9816c29baa6ed80d68513a59f30839d018300c7b3c1c175eaa87c17a7e; s_pers=%20s_fid%3D5CB36F62FC5468A4-052F0C9BE69B3706%7C1654185600438%3B%20s_v%3DY%7C1591115400442%3B%20gpv_p11%3DPersistent%2520Cart%7C1591115400464%3B%20gpv_p44%3Dno%2520value%7C1591115400469%3B%20s_vs%3D1%7C1591115400475%3B; s_sess=%20ent%3DHomepage%3B%20s_cc%3Dtrue%3B%20cps%3D0%3B%20chan%3Dorg%3B%20v59%3D%3B%20v54%3DHomepage%3B%20s_sq%3D%3B',
                        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                        'wg-correlation-id':'60219410-a4e9-11ea-a807-b9e30d7fe127',
                        'x-csrf-jwt':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiaGVhZGVyIiwidXVpZCI6IjA2N2NkYmQwLWE0ZWEtMTFlYS05NWU5LWZiMmQzMmE3ODUwOCIsImlhdCI6MTU5MTExMzU2MiwiZXhwIjoxNTkyMTkzNTYyfQ.bk6H5R1Odayt_uoGwehpKM1-KwIKP8_P0MbXFqmrTfo'
                    })
        

    def final(self,response):
        print(response.body)
