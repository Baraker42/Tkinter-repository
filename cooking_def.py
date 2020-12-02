save_button.grid_forget()
            add_ingredience_entry.grid_forget()
            add_quantity_entry.grid_forget()
            add_unit_entry.grid_forget()
            add_ingredience_label.grid_forget()
            add_quantity_label.grid_forget()
            add_unit_label.grid_forget()

            added_ingredience_label=Label(root, text=added_ingredience)
            added_quantity_label=Label(root, text=added_quantity)
            added_unit_label=Label(root, text=added_unit)

            added_ingredience_label.grid(row=counter,column=1)
            added_quantity_label.grid(row=counter,column=3) 
            added_unit_label.grid(row=counter,column=5)


            global add_ingredience_button
            add_ingredience_button.grid_forget()
            counter=counter+1
            add_ingredience_button=Button(root, text="Přidat další",command=lambda:add_ingredience(chosen,counter))
            add_ingredience_button.grid(row=counter,column=6)
            
