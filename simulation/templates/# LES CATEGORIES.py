 # LES CATEGORIES
    # 'Crise ou Catastrophe Naturelle', 'Crise ou Catastrophe Sanitaire', 'Crise ou Catastrophe Sécuritaire'

    #  LES VITESSE DE PROPAGATIONS
    # 'Maitrisée', 'Lente', 'Rapide'

    # LES FREQUENCE
    # 'Récurrente', 'Non récurrente'

    # LES PROFONDEUR
    # 'Nationale',  'Locale'

    # NIVEAU DE CONTROLE 
    # 'Hors Contrôle', 'Sous Contrôle'

    # NIVEAU DE PERTE 
    # 'Matériel & Humain', 'Matériel'
    if request.method == "POST":
        # print("bonjour")
        cat = request.POST['categorie']
        # print(cat)
    vitessePropagation = request.POST.get('vitessePropagation')
    frequence= request.POST.get('frequence')
    profondeur= request.POST.get('profondeur')
    niveauControle=request.POST.get('niveauControle')
    niveauPerte = request.POST.get('niveauPerte')
    niveaualerte   = request.POST.get('niveaualerte')

 # var.append(categorie)
    # vitessePropagation = request.POST.get('vitessePropagation')
    # var.append(vitessePropagation)

    # frequence= request.POST.get('frequence')
    # var.append(frequence)

    # profondeur= request.POST.get('profondeur')
    # var.append(profondeur)

    # niveauControle=request.POST.get('niveauControle')
    # var.append(niveauControle)

    # niveauPerte = request.POST.get('niveauPerte')
    # var.append(niveauPerte)
    # if  'Crise ou Catastrophe Naturelle' in var and 'Maitrisée' in var and 'Récurrente'     in var and 'Locale'    in var and 'Sous Contrôle' in var and 'Matériel' in var:
    #     print('fiche1')
    #     # return redirect(request, 'simulation.html', {"var":var})
    # elif  'Crise ou Catastrophe Naturelle' in var and 'Maitrisée' in var and 'Récurrente'     in var and 'Nationale'  in var and 'Sous Contrôle' in var and 'Matériel' in var:
    #     print('fiche2')
    #     # return redirect(request, 'simulation.html', {"var":var})

    # elif  'Crise ou Catastrophe Naturelle' in var and 'Maitrisée' in var and 'Non récurrente' in var and 'Locale'     in var and 'Sous Contrôle' in var and 'Matériel' in var:
    #     return redirect(request, 'simulation.html', {"var":var})

    # elif 'Crise ou Catastrophe Naturelle' in var and  'Maitrisée' in var and 'Non récurrente' in var and 'Nationale'  in var and 'Sous Contrôle' in var and 'Matériel' in var:
    #     print('fiche4')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # elif 'Crise ou Catastrophe Naturelle' in var and 'Lente' in      var and 'Récurrente'     in var and 'Locale'     in var and 'Sous Contrôle' in var and 'Matériel' in var:
    #     print('fiche5')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # # elif 'Crise ou Catastrophe Naturelle' in var and 'Lente' in      var and 'Récurrente'     in var and 'Locale'     in var and 'Hors Contrôle' in var and 'Matériel & Humain' in var:

    # elif 'Crise ou Catastrophe Naturelle' in var and 'Lente' in var and 'Récurrente' in var and 'Locale' in var and 'Hors Contrôle' in var and 'Matériel & Humain' in var:
    #     print('fiche6')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # elif 'Crise ou Catastrophe Naturelle' in var and 'Lente' in      var and 'Récurrente'     in var and 'Nationale'  in var and 'Sous Contrôle' in var and 'Matériel' in var:
    #     print('fiche7')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # elif 'Crise ou Catastrophe Naturelle' in var and 'Lente' in      var and 'Récurrente'     in var and 'Nationale'  in var and 'Hors Contrôle' in var and 'Matériel & Humain' in var:
    #     print('fiche8')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # elif 'Crise ou Catastrophe Naturelle' in var and 'Lente' in      var and 'Non récurrente' in var and 'Locale'     in var and 'Sous Contrôle' in var and 'Matériel' in var:
    #     print('fiche9')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # elif 'Crise ou Catastrophe Naturelle' in var and 'Lente' in      var and 'Non récurrente' in var and 'Locale'     in var and 'Hors Contrôle' in var and 'Matériel & Humain' in var:
    #     print('fiche10')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # elif 'Crise ou Catastrophe Naturelle' in var and 'Lente' in     var and 'Non récurrente' in var and 'Nationale'  in var and 'Sous Contrôle' in var and 'Matériel' in var:
    #     print('fiche11')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # elif 'Crise ou Catastrophe Naturelle' in var and 'Rapide' in    var and 'Non récurrente' in var and 'Nationale'  in var and 'Hors Contrôle' in var and 'Matériel & Humain' in var:
    #     print('fiche12')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # elif 'Crise ou Catastrophe Naturelle' in var and 'Rapide' in    var and 'Récurrente'     in var and 'Locale'     in var and 'Sous Contrôle' in var and 'Matériel' in var:
    #     print('fiche13')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # elif 'Crise ou Catastrophe Naturelle' in var and 'Rapide' in    var and 'Récurrente'     in var and 'Locale'     in var and 'Hors Contrôle' in var and 'Matériel & Humain' in var:
    #     print('fiche14')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # elif 'Crise ou Catastrophe Naturelle' in var and 'Rapide' in    var and 'Récurrente'     in var and 'Nationale'  in var and 'Sous Contrôle' in var and 'Matériel' in var:
    #     print('fiche15')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # elif 'Crise ou Catastrophe Naturelle' in var and 'Rapide' in    var and 'Récurrente'     in var and 'Nationale'  in var and 'Hors Contrôle' in var and 'Matériel & Humain' in var:
    #     print('fiche16')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # elif 'Crise ou Catastrophe Naturelle' in var and 'Rapide' in    var and 'Non récurrente' in var and 'Locale'     in var and 'Sous Contrôle' in var and 'Matériel' in var:
    #     print('fiche17')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # elif 'Crise ou Catastrophe Naturelle' in var and 'Rapide' in    var and 'Non récurrente' in var and 'Locale'     in var and 'Hors Contrôle' in var and 'Matériel & Humain' in var:
    #     print('fiche18')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # elif 'Crise ou Catastrophe Naturelle' in var and 'Rapide' in    var and 'Non récurrente' in var and 'Nationale'  in var and 'Sous Contrôle' in var and 'Matériel' in var:
    #     print('fiche19')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # elif 'Crise ou Catastrophe Naturelle' in var and 'Rapide' in    var and 'Non récurrente' in var and 'Nationale'  in var and 'Hors Contrôle' in var and 'Matériel & Humain' in var:
    #     print('fiche20')
    #     # return redirect(request, 'simulation.html', {"var":var})


    # else:
    #     print("raté")

            <!-- <button class="btn btn-success" type="submit" name="save" id="recup_checked"><a href="{% url 'simulation' %}">save</a></button> -->
