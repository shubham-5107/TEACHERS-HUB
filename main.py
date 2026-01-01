from tkinter import *
import random
import time
import subprocess

def cache_file_generator():
    with open(r'Databases/pyq_database.py') as f:
        c= f.read()
    
    with open('cache.py','w') as f:
        f.write('dictionary='+c)


def start_page_interface():
    start_page_interface_window= Tk()
    start_page_interface_window.title("TEACHER'S HUB")
    start_page_interface_window.geometry('1100x618')
    start_page_interface_window.resizable(False,False)

    def about_us_interface():
        about_us_interface_window= Tk()
        about_us_interface_window.geometry('1100x602')
        about_us_interface_window.resizable(False,False)
        about_us_interface_window.title("TEACHER'S HUB")
        about_us_interface_window_bg_img= PhotoImage(file=r'Images/About_us_bg.png')
        about_us_interface_window_bg= Label(about_us_interface_window,image=about_us_interface_window_bg_img).place(relheight=1,relwidth=1)
        def home_page_interface_window_retriver():
            about_us_interface_window.destroy()
            start_page_interface()
        Button(
            about_us_interface_window,
            text='HOME',
            width= 7,
            height=1,
            borderwidth=0,
            bg= '#2B2B2B',
            fg= 'white',
            activebackground='#2B2B2B',
            activeforeground='white',
            font=main_font,
            command= home_page_interface_window_retriver
            ).place(x=0,y=0)
        about_us_interface_window.mainloop()

    def tnc_interface():
        tnc_interface_window= Tk()
        tnc_interface_window.geometry('1100x601')
        tnc_interface_window.resizable(False,False)
        tnc_interface_window.title("TEACHER'S HUB")
        tnc_interface_window_bg_img= PhotoImage(file=r'Images/Terms_and_conditions_bg.png')
        tnc_interface_window_bg= Label(tnc_interface_window,image=tnc_interface_window_bg_img).place(relheight=1,relwidth=1)
        def home_page_interface_window_retriver():
            tnc_interface_window.destroy()
            start_page_interface()
        Button(
            tnc_interface_window,
            text='HOME',
            width= 7,
            height=1,
            borderwidth=0,
            bg= '#2B2B2B',
            fg= 'white',
            activebackground='#2B2B2B',
            activeforeground='white',
            font=main_font,
            command= home_page_interface_window_retriver
            ).place(x=0,y=0)
        tnc_interface_window.mainloop()

    def home_page_interface():
        home_page_interface_window= Tk()
        home_page_interface_window.title("TEACHER'S HUB")
        home_page_interface_window.geometry('1100x618')
        home_page_interface_window.resizable(False,False)
        home_page_interface_window_img= PhotoImage(file=r'Images/Home_bg.png')
        home_page_interface_window_bg= Label(home_page_interface_window,image=home_page_interface_window_img).place(relheight=1,relwidth=1)

        
        def pyq_database_generator_interface():
            pyq_database_generator_interface_window= Tk()
            pyq_database_generator_interface_window.title("TEACHER'S HUB")
            pyq_database_generator_interface_window.geometry('1100x618')
            pyq_database_generator_interface_window.resizable(False,False)
            pyq_database_generator_interface_window_bg_img= PhotoImage(file= r'Images/pyq_database_generator_bg.png')
            pyq_database_generator_interface_window_bg=  Label(pyq_database_generator_interface_window,image=pyq_database_generator_interface_window_bg_img).place(relheight=1,relwidth=1)


            def home_page_interface_window_retriver():
                pyq_database_generator_interface_window.destroy()
                home_page_interface()
                
            home_page_button= Button(
                pyq_database_generator_interface_window,
                text='HOME',
                width= 6,
                height=1,
                borderwidth=0,
                bg= '#D21863',
                fg= 'white',
                activebackground='#D21863',
                activeforeground='white',
                font= main_font,
                command= home_page_interface_window_retriver
                ).place(x=840,y=15)

            cache_file_generator()
            import cache
            
            dictionary= cache.dictionary

            def input_data_retriver():
                retrived_inp_marks= a.get()
                retrived_inp_question_type= b.get()
                retrived_inp_question_statement=c.get()
                retrived_inp_option_a=d.get()
                retrived_inp_option_b=e.get()
                retrived_inp_option_c=f.get()
                retrived_inp_option_d=g.get()

                if retrived_inp_question_type== 'mcq':
                    question_list= [retrived_inp_question_statement,retrived_inp_option_a,retrived_inp_option_b,retrived_inp_option_c,retrived_inp_option_d]
                else:
                    question_list=[retrived_inp_question_statement]
                    
                processed_question= '\n'.join(question_list)
                

                for database_marks in dictionary:
                    for database_question_type in dictionary[database_marks]:
                        if retrived_inp_marks==database_marks:
                            if retrived_inp_question_type==database_question_type:
                                if retrived_inp_question_statement in dictionary[database_marks][database_question_type]:
                                    Label(pyq_database_updater_interface,text='Question already exists in the database....').place(x= 900,y=500)
                                    
                                    
                                    break
                                else:
                                    dictionary[database_marks][database_question_type].append(processed_question)
                                    Label(pyq_database_generator_interface_window,text='database_updated').place(x= 900,y=500)
                                    
                                    break
                                
                with open(r'Databases/pyq_database.py','w') as f1:
                    content= f'{dictionary}'
                    f1.write(content)
                

            a,b,c,d,e,f,g= StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar(),StringVar()

            inp_marks=  Entry(
                pyq_database_generator_interface_window,
                textvariable=a,
                font='16'
                ).place(x= 450,y=190)
            inp_question_type= Entry(
                pyq_database_generator_interface_window,
                textvariable=b,
                font='16'
                ).place(x= 450,y=240)
            inp_question= Entry(
                pyq_database_generator_interface_window,
                textvariable=c,
                width=60,
                font='16'
                ).place(x= 450,y=290)
            inp_option_a= Entry(
                pyq_database_generator_interface_window,
                textvariable=d,
                font='16'
                ).place(x= 450,y=385)
            inp_option_b=Entry(
                pyq_database_generator_interface_window,
                textvariable=e,
                font='16'
                ).place(x= 450,y=435)
            inp_option_c=Entry(
                pyq_database_generator_interface_window,
                textvariable=f,
                font='16'
                ).place(x= 450,y=485)
            inp_option_d= Entry(
                pyq_database_generator_interface_window,
                textvariable=g,
                font='16'
                ).place(x= 450,y=535)

            Button(
                pyq_database_generator_interface_window,
                text='SUBMIT',
                width= 8,
                borderwidth=0,
                bg= '#D21863',
                fg= 'white',
                activebackground='#D21863',
                activeforeground='white',
                font=('Arial',16),
                command=lambda:input_data_retriver()
                ).place(x= 900,y=400)
            
            pyq_database_generator_interface_window.mainloop()
            
        def test_paper_generator_interface():
            test_paper_generator_interface_window= Tk()
            test_paper_generator_interface_window.title("TEACHER'S HUB")
            test_paper_generator_interface_window.resizable(False,False)
            test_paper_generator_interface_window.geometry('1100x618')
            test_paper_generator_interface_window_bg_img= PhotoImage(file= r'Images/testpaper_generator_bg.png')
            test_paper_generator_interface_window_bg=  Label(test_paper_generator_interface_window,image=test_paper_generator_interface_window_bg_img).place(relheight=1,relwidth=1)

            def home_page_interface_window_retriver():
                test_paper_generator_interface_window.destroy()
                home_page_interface()
                
            home_page_button= Button(
                test_paper_generator_interface_window,
                text='HOME',
                width= 6,
                height=1,
                borderwidth=0,
                bg= '#D21863',
                fg= 'white',
                activebackground='#D21863',
                activeforeground='white',
                font= main_font,
                command= home_page_interface_window_retriver
                ).place(x=840,y=15)
            def submit_data_operator():
                def test_paper_frequency_reader():
                    with open(r'Databases/Frequency.txt','r') as f:
                        frequency= f.read()
                        return frequency
                        
                def test_paper_frequency_updater():
                    frequency= test_paper_frequency_reader()
                    with open(r'Databases/Frequency.txt','w') as f:
                        f.write(str(int(frequency)+1))

                cache_file_generator()
                
                content=''
                write_question_type=''
                import cache
                dictionary= cache.dictionary

                inp_question_marks= (a.get()).lower()
                inp_question_type= (b.get()).lower()

                try:
                    inp_subquestion_frequency= int(c.get())
                except ValueError:
                    pass

                if inp_question_type== 'mcq':
                    write_question_type= 'Choose the correct option:'
                elif inp_question_type== 'tnf':
                    write_question_type= 'State whether the following statements are True or False:'
                elif inp_question_type== 'anr':
                    write_question_type= '''Assertion and Reason Type: 
            Each question consists of two statements,namely,Assertion (A) and Reason (R).For selecting the correct answer,use the following code:
            (a) Both Assertion (A) and Reason (R) are the true and Reason (R) is a correct explanation of Assertion (A).
            (b) Both Assertion (A) and Reason (R) are the true but Reason (R) is not a correct explanation of Assertion (A).
            (c) Assertion (A) is true and Reason (R) is false.
            (d) Assertion (A) is false and Reason (R) is true.'''
                elif inp_question_type == 'sa':
                    write_question_type= 'Answer the following questions.'
                elif inp_question_type== 'la':
                    write_question_type= 'Answer the following questions.'
                elif inp_question_type== 'msq':
                    write_question_type= 'Answer the following questions.'
                elif inp_question_type== 'vla':
                    write_question_type= 'Answer the following questions.'

                for question_marks in dictionary:
                    for question_type in dictionary[question_marks]:
                        content_list=[]
                        subquestion_number=1
                                
                        if inp_question_marks == question_marks:
                            if inp_question_type == question_type:
                                try:
                                    content_raw_list=random.sample(dictionary[question_marks][question_type],inp_subquestion_frequency)
                                            
                                    for subquestion in content_raw_list:
                                        question=str(subquestion_number)+'. '+subquestion
                                        content_list+= [question]
                                        subquestion_number+=1

                                    content= '\n'.join(content_list)

                                    with open(f'Testpapers//Testpaper{test_paper_frequency_reader()}.txt','a+') as f:
                                        question_heading_list= ['Q.',write_question_type]
                                        question_heading= ''.join(question_heading_list)

                                        f.write(question_heading)
                                        f.write('\n')
                                        f.write(content)
                                        f.write('\n')
                                        f.write('\n')
                                                
                                                

                                except ValueError:
                                    print('Not enough questions in database to fulfill requirement.....')

                time.sleep(5)
                home_page_interface_window_retriver()
                test_paper_frequency_updater()
                    
            def continue_data_operator():
                def test_paper_frequency_reader():
                    with open(r'Databases/Frequency.txt','r') as f:
                        frequency= f.read()
                        return frequency
                        
                def test_paper_frequency_updater():
                    frequency= test_paper_frequency_reader()
                    with open(r'Databases/Frequency.txt','w') as f:
                        f.write(str(int(frequency)+1))

                cache_file_generator()
                
                content=''
                write_question_type=''
                import cache
                dictionary= cache.dictionary

                inp_question_marks= (a.get()).lower()
                inp_question_type= (b.get()).lower()
                inp_subquestion_frequency= int(c.get())

                if inp_question_type== 'mcq':
                    write_question_type= 'Choose the correct option:'
                elif inp_question_type== 'tnf':
                    write_question_type= 'State whether the following statements are True or False:'
                elif inp_question_type== 'anr':
                    write_question_type= '''Assertion and Reason Type: 
            Each question consists of two statements,namely,Assertion (A) and Reason (R).For selecting the correct answer,use the following code:
            (a) Both Assertion (A) and Reason (R) are the true and Reason (R) is a correct explanation of Assertion (A).
            (b) Both Assertion (A) and Reason (R) are the true but Reason (R) is not a correct explanation of Assertion (A).
            (c) Assertion (A) is true and Reason (R) is false.
            (d) Assertion (A) is false and Reason (R) is true.'''
                elif inp_question_type == 'sa':
                    write_question_type= 'Answer the following questions.'
                elif inp_question_type== 'la':
                    write_question_type= 'Answer the following questions.'
                elif inp_question_type== 'msq':
                    write_question_type= 'Answer the following questions.'
                elif inp_question_type== 'vla':
                    write_question_type= 'Answer the following questions.'

                for question_marks in dictionary:
                    for question_type in dictionary[question_marks]:
                        content_list=[]
                        subquestion_number=1
                                
                        if inp_question_marks == question_marks:
                            if inp_question_type == question_type:
                                try:
                                    content_raw_list=random.sample(dictionary[question_marks][question_type],inp_subquestion_frequency)
                                            
                                    for subquestion in content_raw_list:
                                        question=str(subquestion_number)+'. '+subquestion
                                        content_list+= [question]
                                        subquestion_number+=1

                                    content= '\n'.join(content_list)

                                    with open(f'Testpapers//Testpaper{test_paper_frequency_reader()}.txt','a+') as f:
                                        question_heading_list= ['Q.',write_question_type]
                                        question_heading= ''.join(question_heading_list)

                                        f.write(question_heading)
                                        f.write('\n')
                                        f.write(content)
                                        f.write('\n')
                                        f.write('\n')
                                                
                                                

                                except ValueError:
                                    print('Not enough questions in database to fulfill requirement.....')

            a,b,c=StringVar(),StringVar(),StringVar()
            inp_question_marks_entry= Entry(
                test_paper_generator_interface_window,
                textvariable=a,
                font=16
                ).place(x=550,y=248)
            inp_question_type_entry= Entry(
                test_paper_generator_interface_window,
                textvariable=b,
                font=16
                ).place(x=550,y=318)
            inp_subquestion_frequency= Entry(
                test_paper_generator_interface_window,
                textvariable=c,
                font=16
                     ).place(x=550,y=393)
            Button(
                test_paper_generator_interface_window,
                text='Continue',
                width= 8,
                borderwidth=0,
                bg= '#D21863',
                fg= 'white',
                activebackground='#D21863',
                activeforeground='white',
                font=('Arial',16),
                command=continue_data_operator
                   ).place(x=600,y=480)
            Button(
                test_paper_generator_interface_window,
                text='Submit',
                width= 7,
                borderwidth=0,
                bg= '#D21863',
                fg= 'white',
                activebackground='#D21863',
                activeforeground='white',
                font=('Arial',16),
                command=submit_data_operator
                ).place(x=900,y=480)
            Label(
                test_paper_generator_interface_window,
                text= "Note: Re-enter the value after pressing continue button",
                font= ('Arial',16),
                bg='White'
                ).place(x=350,y=550)
            
            test_paper_generator_interface_window.mainloop()
            
        def omr_sheet_checker_interface():
            omr_sheet_checker_interface_window= Tk()
            omr_sheet_checker_interface_window.title("TEACHER'S HUB")
            omr_sheet_checker_interface_window.geometry('1100x618')
            omr_sheet_checker_interface_window_bg_img= PhotoImage(file= r'Images/omr_checker_bg.png')
            omr_sheet_checker_interface_window_bg=  Label(omr_sheet_checker_interface_window,image=omr_sheet_checker_interface_window_bg_img).place(relheight=1,relwidth=1)

            def home_page_interface_window_retriver():
                omr_sheet_checker_interface_window.destroy()
                home_page_interface()

            home_page_button= Button(
                omr_sheet_checker_interface_window,
                text='HOME',
                width= 6,
                height=1,
                borderwidth=0,
                bg= '#D21863',
                fg= 'white',
                activebackground='#D21863',
                activeforeground='white',
                font= main_font,
                command= home_page_interface_window_retriver
                ).place(x=840,y=15)
            omr_sheet_checker_interface_window.mainloop()

        def shortcuts_interface():
            shortcuts_interface_window= Tk()
            shortcuts_interface_window.title("TEACHER'S HUB")
            shortcuts_interface_window.geometry('1100x618')
            shortcuts_interface_window.resizable(False,False)
            shortcuts_interface_window_bg_img= PhotoImage(file= r'Images/shortcut_bg.png')
            pyq_database_generator_interface_window_bg=  Label(shortcuts_interface_window,image=shortcuts_interface_window_bg_img).place(relheight=1,relwidth=1)

            def home_page_interface_window_retriver():
                shortcuts_interface_window.destroy()
                home_page_interface()
                
            home_page_button= Button(
                shortcuts_interface_window,
                text='HOME',
                width= 6,
                height=1,
                borderwidth=0,
                bg= '#D21863',
                fg= 'white',
                activebackground='#D21863',
                activeforeground='white',
                font= main_font,
                command= home_page_interface_window_retriver
                ).place(x=840,y=15)

            def chrome_retriver():
                subprocess.call("C:\Program Files\Google\Chrome\Application\chrome.exe")
            def notepad_retriver():
                subprocess.call('notepad')
            def calculator_retriver():
                subprocess.call('calc')

            chrome_img= PhotoImage(file=r'Images/chrome.png' )
            notepad_img= PhotoImage(file=r'Images/notepad.png' )

            calculator_img= PhotoImage(file=r'Images/calculator.png' )
            chrome_executor= Button(
                shortcuts_interface_window,
                command=chrome_retriver,
                image= chrome_img,
                activebackground='white',
                borderwidth=0,
                ).place(x=290,y=280)
            notepad_executor= Button(
                shortcuts_interface_window,
                command=notepad_retriver,
                image= notepad_img,
                activebackground='white',
                borderwidth=0
                ).place(x=570,y=280)
            calculator_executor= Button(
                shortcuts_interface_window,
                command=calculator_retriver,
                image= calculator_img,
                activebackground='white',
                borderwidth=0
                ).place(x=870,y=280)
            
            shortcuts_interface_window.mainloop()

        def student_database_interface():
            student_database_interface_window= Tk()
            student_database_interface_window.title("TEACHER'S HUB")
            student_database_interface_window.geometry('1100x618')
            student_database_interface_window.resizable(False,False)
            student_database_interface_window_img= PhotoImage(file=r'Images/student_db_bg.png')
            student_database_interface_window_bg= Label(student_database_interface_window,image=student_database_interface_window_img).place(relheight=1,relwidth=1)
            def home_page_interface_window_retriver():
                student_database_interface_window.destroy()
                home_page_interface()
                
            home_page_button= Button(
                student_database_interface_window,
                text='HOME',
                width= 6,
                height=1,
                borderwidth=0,
                bg= '#D21863',
                fg= 'white',
                activebackground='#D21863',
                activeforeground='white',
                font= main_font,
                command= home_page_interface_window_retriver
                ).place(x=840,y=15)
            student_database_bg_img= PhotoImage(file=r'Images/Student_db_img.PNG')
            Label(student_database_interface_window,image= student_database_bg_img).place(x=235,y=200)
            student_database_interface_window.mainloop()

        def student_fees_database_interface():
            student_fees_database_interface_window= Tk()
            student_fees_database_interface_window.title("TEACHER'S HUB")
            student_fees_database_interface_window.geometry('1100x618')
            student_fees_database_interface_window.resizable(False,False)
            student_fees_database_interface_window_img= PhotoImage(file=r'Images/student_fees_db_bg.png')
            student_fees_database_interface_window_bg= Label(student_fees_database_interface_window,image=student_fees_database_interface_window_img).place(relheight=1,relwidth=1)

            def home_page_interface_window_retriver():
                student_fees_database_interface_window.destroy()
                home_page_interface()
                
            home_page_button= Button(
                student_fees_database_interface_window,
                text='HOME',
                width= 6,
                height=1,
                borderwidth=0,
                bg= '#D21863',
                fg= 'white',
                activebackground='#D21863',
                activeforeground='white',
                font= main_font,
                command= home_page_interface_window_retriver
                ).place(x=840,y=15)

            student_fees_database_bg_img= PhotoImage(file=r'Images/Student_fees_database_ing.png')
            Label(student_fees_database_interface_window,image= student_fees_database_bg_img).place(x=325,y=200)
            student_fees_database_interface_window.mainloop()
            
        def about_us_interface_window_retriver():
            home_page_interface_window.destroy()
            about_us_interface()
        def tnc_interface_window_retriver():
            home_page_interface_window.destroy()
            tnc_interface()
        def pyq_database_generator_interface_window_retriver():
            home_page_interface_window.destroy()
            pyq_database_generator_interface()
        def test_paper_generator_interface_window_retriver():
            home_page_interface_window.destroy()
            test_paper_generator_interface()
        def omr_sheet_checker_interface_window_retriver():
            home_page_interface_window.destroy()
            omr_sheet_checker_interface()
        def shortcuts_interface_window_retriver():
            home_page_interface_window.destroy()
            shortcuts_interface()
        def student_database_interface_window_retriver():
            home_page_interface_window.destroy()
            student_database_interface()
        def student_fees_database_interface_window_retriver():
            home_page_interface_window.destroy()
            student_fees_database_interface()
        
        about_us_button= Button(
            home_page_interface_window,
            text='About Us',
            width= 8,
            height=1,
            borderwidth=0,
            bg= '#D21863',
            fg= 'white',
            activebackground='#D21863',
            activeforeground='white',
            font=('Calibri',17),
            command=about_us_interface_window_retriver
            ).place(x=670,y=17)
        tnc_button= Button(
            home_page_interface_window,
            text='Terms and Conditions',
            width=18,
            height=1,
            borderwidth=0,
            bg= '#D21863',
            fg= 'white',
            activebackground='#D21863',
            activeforeground='white',
            font=main_font,
            command=tnc_interface_window_retriver
            ).place(x=785,y=15)

        pyq_database_generator_button_img=PhotoImage(file= r'Images/pyq_generator_logo.png')
        question_paper_generator_button_img= PhotoImage(file= r'Images/Testpaper_generator_logo.png')
        omr_sheet_checker_button_img= PhotoImage(file= r'Images/OMR_checker_logo.png')
        shortcut_button_img= PhotoImage(file=r'Images/shortcuts.png')
        student_database_button_img= PhotoImage(file=r'Images/Student_Database.png')
        student_fees_database_button_img= PhotoImage(file=r'Images/student_fees_Database.png')

        pyq_database_generator_button= Button(
            home_page_interface_window,
            image=pyq_database_generator_button_img,
            borderwidth=0,
            activebackground='white',
            
            command= pyq_database_generator_interface_window_retriver
            ).place(x=250,y=150)
        test_paper_generator_button= Button(
            home_page_interface_window,
            image= question_paper_generator_button_img,
            borderwidth=0,
            activebackground='white',
            command= test_paper_generator_interface_window_retriver
            ).place(x=460,y=150)
        omr_sheet_checker_button= Button(
            home_page_interface_window,
            image= omr_sheet_checker_button_img,
            borderwidth=0,
            activebackground='white',
            command= omr_sheet_checker_interface_window_retriver
            ).place(x=670,y=150)
        shortcuts_button= Button(
            home_page_interface_window,
            image= shortcut_button_img,
            borderwidth=0,
            activebackground='white',
            command= shortcuts_interface_window_retriver
            ).place(x=890,y=150)
        student_database_button= Button(
            home_page_interface_window,
            image= student_database_button_img,
            borderwidth=0,
            activebackground='white',
            command= student_database_interface_window_retriver
            ).place(x=450,y=370)
        student_fees_database_button= Button(
            home_page_interface_window,
            image= student_fees_database_button_img,
            borderwidth=0,
            activebackground='white',
            command= student_fees_database_interface_window_retriver
            ).place(x=670,y=370)
        home_page_interface_window.mainloop()

    def sign_in_interface():        
        sign_in_interface_window= Tk()
        sign_in_interface_window.geometry('1100x618')
        sign_in_interface_window.resizable(False,False)
        sign_in_interface_window.title("TEACHER'S HUB")

        def start_page_interface_window_retriver():
            sign_in_interface_window.destroy()
            start_page_interface()
        
        sign_in_interface_window_bg_img= PhotoImage(file=r'Images/Sign_in_bg.png')
        sign_in_interface_window_bg= Label(sign_in_interface_window,image=sign_in_interface_window_bg_img).place(relheight=1,relwidth=1)
        start_page_interface_window_retriver_button=Button(
            sign_in_interface_window,
            text='HOME',
            width= 6,
            height=1,
            borderwidth=0,
            bg= '#D21863',
            fg= 'white',
            activebackground='#D21863',
            activeforeground='white',
            font= main_font,
            command= start_page_interface_window_retriver
            ).place(x=840,y=15)

        def home_page_interface_retriver():
            sign_in_interface_window.destroy()
            
            home_page_interface()

        def data_retriver():
            inp_user_id= a.get()
            inp_pswd= b.get()

            if inp_user_id== 'Shubham'and inp_pswd=='abcd':
                home_page_interface_retriver()
            
            else:
                Label(
                    sign_in_interface_window,
                    text='Access Denied',
                    font=('Arial',16),
                    bg='white'
                    ).place(x=400,y=550)
                
        
        a,b= StringVar(),StringVar()
        user_id_inp=Entry(
            sign_in_interface_window,
            width=25,
            font= '16',
            textvariable=a,
            ).place(x=270,y=305)
        pswd_inp= Entry(
            sign_in_interface_window,
            width=25,
            font= '16',
            show= '*',
            textvariable=b
            ).place(x=270,y=380)
        continue_button=Button(
            sign_in_interface_window,
            text='Sign in',
            width= 8,
            height=1,
            borderwidth=0,
            bg= '#D21863',
            fg= 'white',
            activebackground='#D21863',
            activeforeground='white',
            font= main_font,
            command=lambda:data_retriver()
            ).place(x=400,y=450)

        sign_in_interface_window.mainloop()

    def login_interface():
        login_interface_window= Tk()
        login_interface_window.geometry('1100x618')
        login_interface_window.resizable(False,False)
        login_interface_window.title("TEACHER'S HUB")
        
        def home_page_interface_window_retriver():
            login_interface_window.destroy()
            start_page_interface()
        def sign_in_interface_retriver():
            login_interface_window.destroy()
            sign_in_interface()
        def home_page_interface_retriver():
            login_interface_window.destroy()
            
            home_page_interface()

        def data_retriver():
            inp_user_id= a.get()
            inp_pswd= b.get()

            if inp_user_id== 'Shubham'and 'abcd':
                home_page_interface_retriver()
            elif inp_user_id== 'Zaid'and 'abcd':
                home_page_interface_retriver()
            elif inp_user_id== 'Shobhit'and 'abcd':
                home_page_interface_retriver()
            else:
                Label(
                    login_interface_window,
                    text='Access Denied',
                    font=('Arial',16),
                    bg='white'
                    ).place(x=400,y=550)

        login_interface_window_bg_img=PhotoImage(file=r'Images/login_form_bg.png')
        login_interface_window_bg= Label(login_interface_window,image=login_interface_window_bg_img).place(relheight=1,relwidth=1)

        start_page_interface_window_retriver_button=Button(
            login_interface_window,
            text='HOME',
            width= 6,
            height=1,
            borderwidth=0,
            bg= '#D21863',
            fg= 'white',
            activebackground='#D21863',
            activeforeground='white',
            font= main_font,
            command= home_page_interface_window_retriver
            ).place(x=840,y=15)

        a,b= StringVar(),StringVar()
        user_id_inp=Entry(
            login_interface_window,
            textvariable=a,
            width=25,
            font= '16',
            ).place(x=250,y=310)
        pswd_inp= Entry(
            login_interface_window,
            width=25,
            font= '16',
            show= '*',
            textvariable=b
            ).place(x=250,y=385)
        continue_button=Button(
            login_interface_window,
            text='Continue',
            width= 8,
            borderwidth=0,
            bg= '#D21863',
            fg= 'white',
            activebackground='#D21863',
            activeforeground='white',
            font=('Arial',16),
            command=lambda:data_retriver()
            ).place(x=400,y=450)

        sign_in_button= Button(
            login_interface_window,
            text='Sign in',
            width= 10,
            height=1,
            borderwidth=0,
            bg= '#D21863',
            fg= 'white',
            activebackground='#D21863',
            activeforeground='white',
            font= main_font,
            command= sign_in_interface_retriver
            ).place(x=840,y=410)

        login_interface_window.mainloop()


    start_window_bg_img= PhotoImage(file= r'Images/Start_window_bg.png')
    start_button_img= PhotoImage(file= r'Images/start_button.png')
    main_font= ('Calibri',18)
    start_window_bg= Label(start_page_interface_window,image=start_window_bg_img).place(relheight=1,relwidth=1)

    def about_us_interface_window_retriver():
        start_page_interface_window.destroy()
        about_us_interface()
    def tnc_interface_window_retriver():
        start_page_interface_window.destroy()
        tnc_interface()
    def sign_in_interface_window_retriver():
        start_page_interface_window.destroy()
        sign_in_interface()
    def login_interface_window_retriver():
        start_page_interface_window.destroy()
        login_interface()
    start_button= Button(
        start_page_interface_window,
        image=start_button_img,
        borderwidth=0,
        bg= '#39B684',
        activebackground='#39B684',
        command=login_interface_window_retriver
        ).place(x=150,y=420)

    login_button= Button(
        start_page_interface_window,
        text='Login',
        width= 4,
        height=1,
        border=0,
        bg= '#D21863',
        fg= 'white',
        activebackground='#D21863',
        activeforeground='white',
        font= main_font,
        command=login_interface_window_retriver
        ).place(x=510,y=15)

    sign_in_button= Button(
        start_page_interface_window,
        text='Sign in',
        width= 5,
        height=1,
        borderwidth=0,
        bg= '#D21863',
        fg= 'white',
        activebackground='#D21863',
        activeforeground='white',
        font= main_font,
        command=sign_in_interface_window_retriver
        ).place(x=590,y=15)

    about_us_button= Button(
        start_page_interface_window,
        text='About Us',
        width= 8,
        height=1,
        borderwidth=0,
        bg= '#D21863',
        fg= 'white',
        activebackground='#D21863',
        activeforeground='white',
        font=('Calibri',17),
        command=about_us_interface_window_retriver
        ).place(x=670,y=16)

    tnc_button= Button(
        start_page_interface_window,
        text='Terms and Conditions',
        width= 18,
        height=1,
        borderwidth=0,
        bg= '#D21863',
        fg= 'white',
        activebackground='#D21863',
        activeforeground='white',
        font=main_font,
        command=tnc_interface_window_retriver
        ).place(x=790,y=15)
        
        
    start_page_interface_window.mainloop()

if __name__ == '__main__':
    #sql_database_generator()
    start_page_interface()
