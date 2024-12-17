load_dotenv() # load all the variables from the env file
@bot.slash_command(name="clan", description="Say hello to the bot")
async def clan(ctx: discord.ApplicationContext,clan="fgh",arg2="a"):
    clan=clan.lower()
    arg2=arg2.lower()

    if clan=="banu_haqim":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Banu_Haqim_all_embed=discord.Embed(title="Banu Haqim",description=Banu_Haqim_Info+"\n \n"+Banu_Haqim_Disciplines+"\n \n" +Banu_Haqim_Bane+"\n \n"+Banu_Haqim_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Banu_Haqim_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Banu_Haqim_embed=discord.Embed(title="Banu Haqim ",description=Banu_Haqim_Info,color=discord.Color.blue())
            await ctx.send(embed=Banu_Haqim_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            Banu_Haqim_Disciplines_embed=discord.Embed(title="Banu Haqim Disciplines",description=Banu_Haqim_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=Banu_Haqim_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            Banu_Haqim_Bane_embed=discord.Embed(title="Banu Haqim Bane",description=Banu_Haqim_Bane,color=discord.Color.blue())
            await ctx.send(embed=Banu_Haqim_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            Banu_Haqim_Compulsion_embed=discord.Embed(title="Banu Haqim compulsion",description=Banu_Haqim_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Banu_Haqim_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)
    elif clan=="ls":
        ls_embed=discord.Embed(title="ls",description=ls,color=discord.Color.blue())
        await ctx.send(embed=ls_embed)
    elif clan=="brujah":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Brujah_all_embed=discord.Embed(title="Brujah",description=Brujah_Info+"\n \n"+Brujah_Disciplines+"\n \n" +Brujah_Bane+"\n \n"+Brujah_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Brujah_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Brujah_embed=discord.Embed(title="Brujah",description=Brujah_Info,color=discord.Color.blue())
            await ctx.send(embed=Brujah_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            Brujah_Disciplines_embed=discord.Embed(title="Brujah Disciplines",description=Brujah_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=Brujah_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            Brujah_Bane_embed=discord.Embed(title="Brujah Bane",description=Brujah_Bane,color=discord.Color.blue())
            await ctx.send(embed=Brujah_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            Brujah_Compulsion_embed=discord.Embed(title="Brujah compulsion",description=Brujah_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Brujah_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)    
    elif clan=="gangrel":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Gangrel_all_embed=discord.Embed(title="",description=Gangrel_Info+"\n \n"+Gangrel_Disciplines+"\n \n" +Gangrel_Bane+"\n \n"+Gangrel_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Gangrel_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Gangrel_embed=discord.Embed(title="Gangrel",description=Gangrel_Info,color=discord.Color.blue())
            await ctx.send(embed=Gangrel_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            Gangrel_Disciplines_embed=discord.Embed(title="Gangrel Disciplines",description=Gangrel_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=Gangrel_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            Gangrel_Bane_embed=discord.Embed(title="Gangrel Bane",description=Gangrel_Bane,color=discord.Color.blue())
            await ctx.send(embed=Gangrel_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            Gangrel_Compulsion_embed=discord.Embed(title="Gangrel compulsion",description=Gangrel_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Gangrel_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)
    elif clan=="hecata":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Hecata_all_embed=discord.Embed(title="",description=Hecata_Info+"\n \n"+Hecata_Disciplines+"\n \n" +Hecata_Bane+"\n \n"+Hecata_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Hecata_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Hecata_embed=discord.Embed(title="Hecata",description=Hecata_Info,color=discord.Color.blue())
            await ctx.send(embed=Hecata_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            Hecata_Disciplines_embed=discord.Embed(title="Hecata Disciplines",description=Hecata_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=Hecata_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            Hecata_Bane_embed=discord.Embed(title="Hecata Bane",description=Hecata_Bane,color=discord.Color.blue())
            await ctx.send(embed=Hecata_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            Hecata_Compulsion_embed=discord.Embed(title="Hecata compulsion",description=Hecata_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Hecata_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)
    elif clan=="lasombra":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Lasombra_all_embed=discord.Embed(title="",description=Lasombra_Info+"\n \n"+Lasombra_Disciplines+"\n \n" +Lasombra_Bane+"\n \n"+Lasombra_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Lasombra_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Lasombra_embed=discord.Embed(title="Lasombra",description=Lasombra_Info,color=discord.Color.blue())
            await ctx.send(embed=Lasombra_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            Lasombra_Disciplines_embed=discord.Embed(title="Lasombra Disciplines",description=Lasombra_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=Lasombra_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            Lasombra_Bane_embed=discord.Embed(title="Lasombra Bane",description=Lasombra_Bane,color=discord.Color.blue())
            await ctx.send(embed=Lasombra_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            Lasombra_Compulsion_embed=discord.Embed(title="Lasombra compulsion",description=Lasombra_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Lasombra_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)  
    elif clan=="malkavian":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Malkavian_all_embed=discord.Embed(title="",description=Malkavian_Info+"\n \n"+Malkavian_Disciplines+"\n \n" +Malkavian_Bane+"\n \n"+Malkavian_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Malkavian_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Malkavian_embed=discord.Embed(title="Malkavian",description=Malkavian_Info,color=discord.Color.blue())
            await ctx.send(embed=Malkavian_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            Malkavian_Disciplines_embed=discord.Embed(title="Malkavian Disciplines",description=Malkavian_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=Malkavian_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            Malkavian_Bane_embed=discord.Embed(title="Malkavian Bane",description=Malkavian_Bane,color=discord.Color.blue())
            await ctx.send(embed=Malkavian_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            Malkavian_Compulsion_embed=discord.Embed(title="Malkavian compulsion",description=Malkavian_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Malkavian_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed) 
    elif clan=="the_ministry":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            The_Ministry_all_embed=discord.Embed(title="",description=The_Ministry_Info+"\n \n"+The_Ministry_Disciplines+"\n \n" +The_Ministry_Bane+"\n \n"+The_Ministry_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=The_Ministry_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            The_Ministry_embed=discord.Embed(title="The_Ministry",description=The_Ministry_Info,color=discord.Color.blue())
            await ctx.send(embed=The_Ministry_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            The_Ministry_Disciplines_embed=discord.Embed(title="The_Ministry Disciplines",description=The_Ministry_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=The_Ministry_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            The_Ministry_Bane_embed=discord.Embed(title="The_Ministry Bane",description=The_Ministry_Bane,color=discord.Color.blue())
            await ctx.send(embed=The_Ministry_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            The_Ministry_Compulsion_embed=discord.Embed(title="The_Ministry compulsion",description=The_Ministry_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=The_Ministry_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)    
    elif clan=="Nosferatu":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Nosferatu_all_embed=discord.Embed(title="",description=Nosferatu_Info+"\n \n"+Nosferatu_Disciplines+"\n \n" +Nosferatu_Bane+"\n \n"+Nosferatu_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Nosferatu_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Nosferatu_embed=discord.Embed(title="Nosferatu",description=Nosferatu_Info,color=discord.Color.blue())
            await ctx.send(embed=Nosferatu_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            Nosferatu_Disciplines_embed=discord.Embed(title="Nosferatu Disciplines",description=Nosferatu_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=Nosferatu_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            Nosferatu_Bane_embed=discord.Embed(title="Nosferatu Bane",description=Nosferatu_Bane,color=discord.Color.blue())
            await ctx.send(embed=Nosferatu_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            Nosferatu_Compulsion_embed=discord.Embed(title="Nosferatu compulsion",description=Nosferatu_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Nosferatu_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)
    elif clan=="ravnos":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Ravnos_all_embed=discord.Embed(title="",description=Ravnos_Info+"\n \n"+Ravnos_Disciplines+"\n \n" +Ravnos_Bane+"\n \n"+Ravnos_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Ravnos_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Ravnos_embed=discord.Embed(title="Ravnos",description=Ravnos_Info,color=discord.Color.blue())
            await ctx.send(embed=Ravnos_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            Ravnos_Disciplines_embed=discord.Embed(title="Ravnos Disciplines",description=Ravnos_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=Ravnos_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            Ravnos_Bane_embed=discord.Embed(title="Ravnos Bane",description=Ravnos_Bane,color=discord.Color.blue())
            await ctx.send(embed=Ravnos_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            Ravnos_Compulsion_embed=discord.Embed(title="Ravnos compulsion",description=Ravnos_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Ravnos_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)
    elif clan=="salubri":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Salubri_all_embed=discord.Embed(title="",description=Salubri_Info+"\n \n"+Salubri_Disciplines+"\n \n" +Salubri_Bane+"\n \n"+Salubri_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Salubri_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Salubri_embed=discord.Embed(title="Salubri",description=Salubri_Info,color=discord.Color.blue())
            await ctx.send(embed=Salubri_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            Salubri_Disciplines_embed=discord.Embed(title="Salubri Disciplines",description=Salubri_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=Salubri_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            Salubri_Bane_embed=discord.Embed(title="Salubri Bane",description=Salubri_Bane,color=discord.Color.blue())
            await ctx.send(embed=Salubri_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            Salubri_Compulsion_embed=discord.Embed(title="Salubri compulsion",description=Salubri_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Salubri_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)
    elif clan=="toreador":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Toreador_all_embed=discord.Embed(title="",description=Toreador_Info+"\n \n"+Toreador_Disciplines+"\n \n" +Toreador_Bane+"\n \n"+Toreador_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Toreador_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Toreador_embed=discord.Embed(title="Toreador",description=Toreador_Info,color=discord.Color.blue())
            await ctx.send(embed=Toreador_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            Toreador_Disciplines_embed=discord.Embed(title="Toreador Disciplines",description=Toreador_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=Toreador_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            Toreador_Bane_embed=discord.Embed(title="Toreador Bane",description=Toreador_Bane,color=discord.Color.blue())
            await ctx.send(embed=Toreador_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            Toreador_Compulsion_embed=discord.Embed(title="Toreador compulsion",description=Toreador_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Toreador_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)
    elif clan=="tremere":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Tremere_all_embed=discord.Embed(title="",description=Tremere_Info+"\n \n"+Tremere_Disciplines+"\n \n" +Tremere_Bane+"\n \n"+Tremere_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Tremere_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Tremere_embed=discord.Embed(title="Tremere",description=Tremere_Info,color=discord.Color.blue())
            await ctx.send(embed=Tremere_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            Tremere_Disciplines_embed=discord.Embed(title="Tremere Disciplines",description=Tremere_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=Tremere_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            Tremere_Bane_embed=discord.Embed(title="Tremere Bane",description=Tremere_Bane,color=discord.Color.blue())
            await ctx.send(embed=Tremere_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            Tremere_Compulsion_embed=discord.Embed(title="Tremere compulsion",description=Tremere_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Tremere_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)
    elif clan=="tzimisce":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Tzimisce_all_embed=discord.Embed(title="",description=Tzimisce_Info+"\n \n"+Tzimisce_Disciplines+"\n \n" +Tzimisce_Bane+"\n \n"+Tzimisce_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Tzimisce_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Tzimisce_embed=discord.Embed(title="Tzimisce",description=Tzimisce_Info,color=discord.Color.blue())
            await ctx.send(embed=Tzimisce_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            Tzimisce_Disciplines_embed=discord.Embed(title="Tzimisce Disciplines",description=Tzimisce_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=Tzimisce_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            Tzimisce_Bane_embed=discord.Embed(title="Tzimisce Bane",description=Tzimisce_Bane,color=discord.Color.blue())
            await ctx.send(embed=Tzimisce_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            Tzimisce_Compulsion_embed=discord.Embed(title="Tzimisce compulsion",description=Tzimisce_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Tzimisce_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)
    elif clan=="ventrue":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Ventrue_all_embed=discord.Embed(title="",description=Ventrue_Info+"\n \n"+Ventrue_Disciplines+"\n \n" +Ventrue_Bane+"\n \n"+Ventrue_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Ventrue_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Ventrue_embed=discord.Embed(title="Ventrue",description=Ventrue_Info,color=discord.Color.blue())
            await ctx.send(embed=Ventrue_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            Ventrue_Disciplines_embed=discord.Embed(title="Ventrue Disciplines",description=Ventrue_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=Ventrue_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            Ventrue_Bane_embed=discord.Embed(title="Ventrue Bane",description=Ventrue_Bane,color=discord.Color.blue())
            await ctx.send(embed=Ventrue_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            Ventrue_Compulsion_embed=discord.Embed(title="Ventrue compulsion",description=Ventrue_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Ventrue_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)
        token=file.read()   
    elif clan=="caitiff":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            Caitiff_all_embed=discord.Embed(title="",description=Caitiff_Info+"\n \n"+Caitiff_Disciplines+"\n \n" +Caitiff_Bane+"\n \n"+Caitiff_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Caitiff_all_embed)
        
        elif (arg2=="info")or(arg2=="i"):
            Caitiff_embed=discord.Embed(title="Caitiff",description=Caitiff_Info,color=discord.Color.blue())
            await ctx.send(embed=Caitiff_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            Caitiff_Disciplines_embed=discord.Embed(title="Caitiff Disciplines",description=Caitiff_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=Caitiff_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            Caitiff_Bane_embed=discord.Embed(title="Caitiff Bane",description=Caitiff_Bane,color=discord.Color.blue())
            await ctx.send(embed=Caitiff_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            Caitiff_Compulsion_embed=discord.Embed(title="Caitiff compulsion",description=Caitiff_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=Caitiff_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)
    elif clan=="thin_blood":
        
        
        
        if (arg2=="all") or (arg2=="a"):
            thin_blood_embed=discord.Embed(title="thin_blood",description="not easy being a thin blood even bots don't like you.to much data i think other commans work for thin blood though",color=discord.Color.blue())
            await ctx.send(embed=thin_blood_embed)
            
        
        elif (arg2=="info")or(arg2=="i"):
            thin_blood_embed=discord.Embed(title="thin_blood",description=thin_blood_Info,color=discord.Color.blue())
            await ctx.send(embed=thin_blood_embed)
        
        elif (arg2=="disciplines") or(arg2=="d"):
            thin_blood_Disciplines_embed=discord.Embed(title="thin_blood Disciplines",description=thin_blood_Disciplines,color=discord.Color.blue())
            await ctx.send(embed=thin_blood_Disciplines_embed)
        elif (arg2=="bane") or(arg2=="b"):
            thin_blood_Bane_embed=discord.Embed(title="thin_blood Bane",description=thin_blood_Bane,color=discord.Color.blue())
            await ctx.send(embed=thin_blood_Bane_embed)
        elif (arg2=="compulsion") or(arg2=="c"):
            thin_blood_Compulsion_embed=discord.Embed(title="thin_blood compulsion",description=thin_blood_Compulsion,color=discord.Color.blue())
            await ctx.send(embed=thin_blood_Compulsion_embed)
        
        else:
            error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
            await ctx.send(embed=error_embed)
    else:
        error_embed=discord.Embed(title="error",description=error_clan,color=discord.Color.blue())
        await ctx.send(embed=error_embed)