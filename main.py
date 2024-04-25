import flet as ft
import time
def main(page: ft.Page):
    page.window_height = 700
    page.bgcolor=ft.colors.WHITE
    page.scroll = "auto"
    price = ['$100', '$200', '$1000']
    cont1_text = ft.Text(' RubIcon', size=20, color=ft.colors.BLACK, animate_opacity=300, opacity=0)
    cont2_text = ft.Text(' Camera', size=20, color=ft.colors.BLACK, animate_opacity=300, opacity=0)
    cont3_text = ft.Text(' G Generator', size=20, color=ft.colors.BLACK, animate_opacity=300, opacity=0)
    cont4_text = ft.Text(' Invoice Creator', size=20, color=ft.colors.BLACK, animate_opacity=300, opacity=0)
    
    def github(event):
        
        page.launch_url('https://github.com/alisherkamalov')
        page.update()
    
    def buy1(event):
            cont_in_content2.opacity = 0
            cont_in_content3.opacity = 0
            cont_in_content4.opacity = 0
            btn_buy1.opacity = 0
            time.sleep(0.5)
            page.update()
            btn_buy1.text = 'Purchased'
        
            time.sleep(0.5)
            btn_buy1.opacity = 1
            page.update()
            time.sleep(0.5)
            cont_in_content2.opacity = 1
            cont_in_content3.opacity = 1
            cont_in_content4.opacity = 1
            page.update()
            
    def buy2(event):
            cont_in_content1.opacity = 0
            cont_in_content3.opacity = 0
            cont_in_content4.opacity = 0
            btn_buy2.opacity = 0
            time.sleep(0.5)
            page.update()
            btn_buy2.text = 'Purchased'
        
            time.sleep(0.5)
            btn_buy2.opacity = 1
            page.update()
            time.sleep(0.5)
            cont_in_content1.opacity = 1
            cont_in_content3.opacity = 1
            cont_in_content4.opacity = 1
            page.update()
            
    def buy3(event):
            cont_in_content2.opacity = 0
            cont_in_content1.opacity = 0
            cont_in_content4.opacity = 0
            btn_buy3.opacity = 0
            time.sleep(0.5)
            page.update()
            btn_buy3.text = 'Purchased'
        
            time.sleep(0.5)
            btn_buy3.opacity = 1
            page.update()
            time.sleep(0.5)
            cont_in_content2.opacity = 1
            cont_in_content1.opacity = 1
            cont_in_content4.opacity = 1
            page.update()
            
    def buy4(event):
            cont_in_content2.opacity = 0
            cont_in_content3.opacity = 0
            cont_in_content1.opacity = 0
            btn_buy4.opacity = 0
            time.sleep(0.5)
            page.update()
            btn_buy4.text = 'Purchased'
        
            time.sleep(0.5)
            btn_buy4.opacity = 1
            page.update()
            time.sleep(0.5)
            cont_in_content2.opacity = 1
            cont_in_content3.opacity = 1
            cont_in_content1.opacity = 1
            page.update()
            
        
        
        
    
    btn_buy1 = ft.ElevatedButton(text='Buy', color=ft.colors.WHITE, bgcolor=ft.colors.BLUE_500, animate_opacity=300, opacity=0, width=120, height=50, on_click=buy1)
    btn_buy2 = ft.ElevatedButton(text='Buy', color=ft.colors.WHITE, bgcolor=ft.colors.BLUE_500, animate_opacity=300, opacity=0, width=120, height=50, on_click=buy2)
    btn_buy3 = ft.ElevatedButton(text='Buy', color=ft.colors.WHITE, bgcolor=ft.colors.BLUE_500, animate_opacity=300, opacity=0, width=120, height=50, on_click=buy3)
    btn_buy4 = ft.ElevatedButton(text='Buy', color=ft.colors.WHITE, bgcolor=ft.colors.BLUE_500, animate_opacity=300, opacity=0, width=120, height=50, on_click=buy4)
    cont1_text_price = ft.Text(f' {price[0]}', size=20, color=ft.colors.BLUE_500, animate_opacity=300, opacity=0)
    cont2_text_price = ft.Text(f' {price[1]}', size=20, color=ft.colors.BLUE_500, animate_opacity=300, opacity=0)
    cont3_text_price = ft.Text(f' {price[2]}', size=20, color=ft.colors.BLUE_500, animate_opacity=300, opacity=0)
    cont4_text_price = ft.Text(f' {price[0]}', size=20, color=ft.colors.BLUE_500, animate_opacity=300, opacity=0)
    
    def hover1(event):
        if event.data == 'true':
            event.control.scale = ft.transform.Scale(1)
            cont1_text.opacity = 1
            btn_buy1.opacity = 1
            cont1_text_price.opacity = 1
            page.update()
            
        else:
            event.control.scale = ft.transform.Scale(0.7)
            cont1_text.opacity = 0
            btn_buy1.opacity = 0
            cont1_text_price.opacity = 0
            page.update()
            
    def hover2(event):
        if event.data == 'true':
            event.control.scale = ft.transform.Scale(1)
            cont2_text.opacity = 1
            btn_buy2.opacity = 1
            cont2_text_price.opacity = 1
            page.update()
            
        else:
            event.control.scale = ft.transform.Scale(0.7)
            cont2_text.opacity = 0
            btn_buy2.opacity = 0
            cont2_text_price.opacity = 0
            page.update()
            
            
    def hover3(event):
        if event.data == 'true':
            event.control.scale = ft.transform.Scale(1)
            cont3_text.opacity = 1
            btn_buy3.opacity = 1
            cont3_text_price.opacity = 1
            page.update()
            
        else:
            event.control.scale = ft.transform.Scale(0.7)
            cont3_text.opacity = 0
            btn_buy3.opacity = 0
            cont3_text_price.opacity = 0
            page.update()
            
    def hover4(event):
        if event.data == 'true':
            event.control.scale = ft.transform.Scale(1)
            cont4_text.opacity = 1
            btn_buy4.opacity = 1
            cont4_text_price.opacity = 1
            page.update()
            
        else:
            event.control.scale = ft.transform.Scale(0.7)
            cont4_text.opacity = 0
            btn_buy4.opacity = 0
            cont4_text_price.opacity = 0
            page.update()
    
    cont_in_content1 = ft.Container (
        
        expand=True,
        on_hover=hover1,
        bgcolor=ft.colors.WHITE,
        scale=ft.transform.Scale(0.7),
        animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        border_radius=15,
        animate_opacity=300,
        opacity=1,
        content=ft.Column([
            ft.Image(src='https://s3-alpha-sig.figma.com/img/c09f/51c7/152d2da442f6a800330a0adf28616b44?Expires=1714953600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=m3r4LXJPY44ZI4tt2CbNvzfPWxw4WYzusZI6msx1pijLKCrpnuBhNTTqTxn6oE5VMkCSO5QqKxiOYJwkgdFop55tHC38TO2ov9lzHgRAB6lP5lZCll8c7lW95e8AdNQJyMbLQhEP64aTuMutPbm1PMJFYeGBY58rANQ0ObwjaqAHq~AR4V7LU1K3LK~KoFVfLRduatWJYDjyuS~RooTUwn80Zvd41o~k6k~1JFKlsFn-oIt8AFwpVMzFkIAyVKAK0bBvPBP8Vc6Lx8U2AoNKGDZ~RsWIdUNXioemn9dexVZuyRGbdBp-R--ngbVZdSqxSDoa~FW2f-ONa8ZsQHPqgA__', border_radius=15),
            cont1_text,
            cont1_text_price,
            btn_buy1,
            
        ])
       
    )
    
    cont_in_content2 = ft.Container (
        
        expand=True,
        on_hover=hover2,
        bgcolor=ft.colors.WHITE,
        scale=ft.transform.Scale(0.7),
        animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        border_radius=15,
        animate_opacity=300,
        opacity=1,
        content=ft.Column([
            ft.Image(src='https://s3-alpha-sig.figma.com/img/a21a/16aa/6e5f03add1f373d657d32d7b285af02b?Expires=1714953600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=bEOK0wfeQyMOyUIlvqA7uwDVVEBS8u0z8RYlBruKr6jDLuV93Ea78qtmGz0Db5esmpIh14kC2tPcMPf16EGTR8XGPdvEQGil~RCpmzfknRQHB1IXXTbqoJz4TswhECV1pP5ay9ew2yaS5cib64AHAcoOlC3xbKj3-GO4iPTNkggwRV6cPXpGqnupBENN0KKr6fQUFrfZCnfwm1S9sXcpjOTTeu3Je64n-HOoWazqWBnHeJxv-kdTDGf3Va~sXNQs6NEoHwp7NDU89foAmiMMr8dxqPFvlaDI3RUvYHEpuebnySdMl~hDf9Eh2CFK-JfCzBiHfELiHRgwHtIgR0EGbA__', border_radius=15),
            cont2_text,
            cont2_text_price,
            btn_buy2,
            
        ])
        
    )
    
    cont_in_content3 = ft.Container (
        
        expand=True,
        on_hover=hover3,
        bgcolor=ft.colors.WHITE,
        scale=ft.transform.Scale(0.7),
        animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        border_radius=15,
        animate_opacity=300,
        opacity=1,
        content=ft.Column([
            ft.Image(src='https://s3-alpha-sig.figma.com/img/33d2/ad3e/3d9451782fc6d14777fe4516f4e6b9e1?Expires=1714953600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=cv1h2FBl-pAsllPmVdVMd5c~o8Sdcox1j1LwE3Kmzi~jOZ5W6i7rk41eVWqqVD8VSf9WkOOsm-bEUBJGYDV2AFKs1eUqEfDp00U1~TmUw1ScL09n2IHVpUdMXabBdFI7~NFMckh7Q1g4TVb22DQLERMOda8s2NCqgytw9tS~YkG~smKhhm-rZQSJgej3m6lFnIm7CULiudC9J5FEiXYBSip-rB1uFIEgtiuwVjkyYOLsK5sgtcfKnHVwPM5Wzm7TAGFhR77c~RfKgJ1~KSsXTxr9pTglTK5oA57uaREAJKeH-jum5n3F72wJwXx1aXBHRg~d4CYPhi1sa7YndHo5Ww__', border_radius=15),
            cont3_text,
            cont3_text_price,
            btn_buy3,
            
        ])
        
    )
    cont_in_content4 = ft.Container (
        
        expand=True,
        on_hover=hover4,
        bgcolor=ft.colors.WHITE,
        scale=ft.transform.Scale(0.7),
        animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        border_radius=15,
        animate_opacity=300,
        opacity=1,
        content=ft.Column([
            ft.Image(src='https://s3-alpha-sig.figma.com/img/ea0b/8431/64688c851a81ecd4c47f4037108a4779?Expires=1714953600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=NFP2irhQSDqXOItLm-vnERgDdPjDVMVvPqvFHEwdRlsDsjNp19tutrucgJw3vmaaI24SOgNrT9fs98bqx5FzBqFsKMFx5fwANfFU4ZKuj3eUKLyiQ5~eYF-A1wZ3ukKYC8wB9ePZdsiUio0lCDBZlEwZXKHj9EA9XD3pg2DD2cO~LH6pBQeqeQwt7zRtIoDjlaFuB2jGyeyi5aaqnwQh32Jv9lBMocAeDjvAdE6HYN-xFst6lKyGMmeaNeSqmELMNRNFRy2dnKSSVdKH69MtINQZ3ZhaxSQPHkwEhHuuZq3loKWKumy~egEgftjwFZEp34sG76jrbcCohJCMYMtxRg__', border_radius=15),
            cont4_text,
            cont4_text_price,
            btn_buy4,
            
        ])
    )
    
    
    
    cont_content = ft.Container (
        
        bgcolor=ft.colors.WHITE,
        alignment=ft.alignment.Alignment(-0.5, -0.5),
        content=ft.Column([
            ft.Text('Popular Wordpress Plugins', size=25, color=ft.colors.BLACK),
            ft.Row([
                cont_in_content1,
                cont_in_content2,
                
                
            ]),
            ft.Row([
                cont_in_content3,
                cont_in_content4
            ])
        ])
    )
    
    
    
   
    
    cont_logo = ft.Container (
        ft.Image(src="https://s3-alpha-sig.figma.com/img/dd20/ca6f/a7df96e33f795ec1a5129eaea2567760?Expires=1714953600&Key-Pair-Id=APKAQ4GOSFWCVNEHN3O4&Signature=c2fy7Ho6lfE40MMEZkGEDQsBewFRaJzYwNVD6SGc~T~1q54DrGPk3yHWzf1htVUt6AEfoXyP8v9bkztr3ymGGRVMwdLUulkvMvxfkk50jjVw3x2LrsUs2eDJe1GMaCbwz9Yj~5oAhOcYE8KpUQjUmZBrByaRK4FIlwEbXdceCevJkHmf5VjRSBzSlO3Bvz5weoHMbTLrYt5TMC0WaRzqZLmxOH05rIOV4b~1ucKPJYbM2CvdQLveZPF5BexVh2zhAXE9gHpDV6nl7TxCbM7MsWziy9GRoINGChmWsB7Ujhz1w~ZepFNvfRvl748Xm~p2nkAnNl4kEbEQH9aiBsnCxw__"),
        width=25,
        height=25,
        bgcolor=ft.colors.WHITE,
        alignment=ft.alignment.center,
        on_click=True
    )
    
    
    bottombar = ft.BottomAppBar (
        bgcolor=ft.colors.WHITE,
        shadow_color=ft.colors.GREY_200,
        height=125,
        content=ft.Stack([
            ft.Column([
                ft.Text('© DUGIMAIL. All rights reserved.', size=15, color=ft.colors.GREY_500),
                ft.Text('If you have any questions please contact us alisherkamal404@gmail.com', size=15, color=ft.colors.GREY_500),
                ft.Container (
                    width=50,
                    height=50,
                    bgcolor=ft.colors.WHITE,
                    on_click=github,
                    content=ft.Column([
                        ft.Icon(name=ft.icons.HUB, color=ft.colors.BLACK)])
                )
                
            ])
        ])
        
    )
    
    
    cont_cap = ft.Container (
        height=50,
        bgcolor=ft.colors.WHITE,
        scale=ft.transform.Scale(1.5),
        alignment=ft.alignment.center,
        
        content=ft.Stack([
            cont_logo
        ])
    )
    
    page.add(cont_cap, cont_content, bottombar)
    
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER, port=5252)