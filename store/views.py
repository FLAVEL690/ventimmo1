
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from store.models import Product, Order
from .serializers import storeSerializer ,OrderSerializer



class ListProductView(ListAPIView):
    queryset=Product.objects.all()
    serializer_class= storeSerializer 

class CreateProductView(CreateAPIView):
    queryset=Product.objects.all()
    serializer_class= storeSerializer 

class UpdateProductView(UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class= storeSerializer 

class DeleteProductView(DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class= storeSerializer 

# from django.http import JsonResponse

# def add_to_cart(request, product_id):
#     """
#     Ajoute un produit au panier
#     """
#     product = Product.objects.get(id=product_id)

#     cart = request.session.get('cart', {}) # récupère la session en cours, ou crée un panier vide
#     if product_id in cart:
#         # Incrémente la quantité de produit si elle existe déjà dans le panier
#         cart[product_id]['quantity'] += 1
#     else:
#         # Ajoute le produit au panier avec une quantité initiale de 1
#         cart[product_id] = {'name': product.name, 'price': product.price, 'quantity': 1, 'image': product.image}
    
#     request.session['cart'] = cart # sauvegarde le panier mis à jour dans la session

#     return JsonResponse({'status': 'success', 'message': 'Product added to cart', 'cart': cart})

# def remove_from_cart(request, product_id):
#     """
#     Supprime un produit du panier
#     """
#     cart = request.session.get('cart', {})
    
#     if product_id in cart:
#         del cart[product_id]
#         request.session['cart'] = cart # sauvegarde le panier mis à jour dans la session
        
#         return JsonResponse({'status': 'success', 'message': 'Product removed from cart', 'cart': cart})

#     return JsonResponse({'status': 'error', 'message': 'Product not found in cart'})

# def view_cart(request):
#     """
#     Affiche le contenu du panier
#     """
#     cart = request.session.get('cart', {})
#     return JsonResponse({'status': 'success', 'cart': cart})




class ListOrderView(ListAPIView):
    queryset= Order.objects.all()
    serializer_class= OrderSerializer

class CreateOrderView(CreateAPIView):
    queryset= Order.objects.all()
    serializer_class= OrderSerializer

class UpdateOrderView(UpdateAPIView): 
    queryset= Order.objects.all()
    serializer_class= OrderSerializer

class DeleteOrderView(DestroyAPIView):
    queryset= Order.objects.all()
    serializer_class= OrderSerializer 


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer



def ajouter_au_panier(request, product_id):
    produit = get_object_or_404(Product, pk=product_id)
    panier = request.session.get('panier', {})
    quantite = panier.get(str(product_id), 0)
    panier[str(product_id)] = quantite + 1
    request.session['panier'] = panier
    return JsonResponse({"success":True}, safe=False)

def supprimer_du_panier(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    panier = request.session.get('panier', {})
    if str(produit_id) in panier:
        del panier[str(produit_id)]
        request.session['panier'] = panier
    return JsonResponse({"success":True}, safe=False)


def afficher_panier(request):
    panier = request.session.get('panier', {})
    produits = []
    total = 0
    for produit_id, quantite in panier.items():
        produit = get_object_or_404(Produit, pk=produit_id)
        produits.append({
            'titre': produit.titre,
            'prix': produit.prix,
            'quantite': quantite,
            'total': quantite * produit.prix
        })
        total += quantite * produit.prix
    return JsonResponse({'produits': produits, 'total': total}, safe=False)







