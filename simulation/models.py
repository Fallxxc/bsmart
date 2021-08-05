from django.db import models

# Create your models here.

class Categorie(models.Model):
    cathegorie_name = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.cathegorie_name}"

class VitessePropagation(models.Model):
    vitesse = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.vitesse}"

class Frequence(models.Model):
    frequence = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.frequence}"

class Profondeur(models.Model):
    profondeur = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.profondeur}"

class NiveauControle(models.Model):
    niveau_control = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.niveau_control}"

class NiveauPerte(models.Model):
    niveau_perte = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.niveau_perte}"


class Niveaualerte(models.Model):
    niveau_alerte = models.CharField(max_length = 200, blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.niveau_alerte}"











# def post_api(sender, instance, created, **kwargs):
#     data = {}
#     location = "eu-central-1"
#     if created:
#         data = {
#             "bank_id": str(instance.id),
#             "bank_swift": str(instance.swift),
#             "bank_name": str(instance.name),
#             "bank_logo_url": f'https://{instance.s3_bucket}.s3.{location}.amazonaws.com/{instance.avatar}',
#             "sqs_qrc_processing_in": str(instance.sqs_qrc_processing_in),
#             "sqs_qrc_processing_out": str(instance.sqs_qrc_processing_out),
#             "sqs_customer_in": str(instance.sqs_customer_in),
#             "sqs_customer_out": str(instance.sqs_customer_out),
#             "sqs_transaction_in": str(instance.sqs_transaction_in),
#             "sqs_transaction_out": str(instance.sqs_transaction_out),
#             "sqs_validation_in": str(instance.sqs_validation_in),
#             "sqs_validation_out": str(instance.sqs_validation_out),
#             "s3_bucket": str(instance.s3_bucket),
#           #  "s3_bucket_url":str(instance.s3_bucket_url),
#             "s3_print_bucket": str(instance.s3_print_bucket),
#             "s3_c_exchange_folder": str(instance.s3_c_exchange_folder),
#             "s3_c_internal_foder": str(instance.s3_c_internal_folder),
#         }
#         if data["bank_swift"]=='':
#             data["bank_swift"] = "str"

#         if data["bank_name"]=='':
#             data["bank_name"] = "str"

#         if data["bank_logo_url"]=='':
#             data["bank_logo_url"] = "str"

#         if data["sqs_qrc_processing_in"]=='':
#             data["sqs_qrc_processing_in"] = "str"

#         if data["sqs_qrc_processing_out"]=='':
#             data["sqs_qrc_processing_out"] = "str"

#         if data["sqs_customer_in"]=='':
#             data["sqs_customer_in"] = "str"

#         if data["sqs_customer_out"]=='':
#             data["sqs_customer_out"] = "str"

#         if data["sqs_transaction_in"]=='':
#             data["sqs_transaction_in"] = "str"

#         if data["sqs_transaction_out"]=='':
#             data["sqs_transaction_out"] = "str"

#         if data["sqs_validation_in"]=='':
#             data["sqs_validation_in"] = "str"

#         if data["sqs_validation_out"]=='':
#             data["sqs_validation_out"] = "str"

#         if data["s3_bucket"]=='':
#             data["s3_bucket"] = "str"

#         # if data["s3_bucket_url"]=='':
#         #     data["s3_bucket_url"] = "str"
        
#         if data["s3_print_bucket"]=='':
#             data["s3_print_bucket"] = "str"

#         if data["s3_c_exchange_folder"]=='':
#             data["s3_c_exchange_folder"] = "str"

#         if data["s3_c_internal_foder"]=='':
#             data["s3_c_internal_foder"] = "str"

#         requests.post(settings.DYNAMODB_URL, json=data, headers={"Content-Type": "application/json"})
#     else:
#         data = {
#                 "bank_swift": str(instance.swift),
#                 "bank_name": str(instance.name),
#                 "bank_logo_url": f'https://{instance.s3_bucket}.s3.{location}.amazonaws.com/{instance.avatar}',
#                 "sqs_qrc_processing_in": str(instance.sqs_qrc_processing_in),
#                 "sqs_qrc_processing_out": str(instance.sqs_qrc_processing_out),
#                 "sqs_customer_in": str(instance.sqs_customer_in),
#                 "sqs_customer_out": str(instance.sqs_customer_out),
#                 "sqs_transaction_in": str(instance.sqs_transaction_in),
#                 "sqs_transaction_out": str(instance.sqs_transaction_out),
#                 "sqs_validation_in": str(instance.sqs_validation_in),
#                 "sqs_validation_out": str(instance.sqs_validation_out),
#                 "s3_bucket": str(instance.s3_bucket),
#                 #"s3_bucket_url":str(instance.s3_bucket_url),
#                 "s3_print_bucket": str(instance.s3_print_bucket),
#                 "s3_c_exchange_folder": str(instance.s3_c_exchange_folder),
#                 "s3_c_internal_foder": str(instance.s3_c_internal_folder),
#         }
#         if data["bank_swift"]=='':
#             data["bank_swift"] = "str"

#         if data["bank_name"]=='':
#             data["bank_name"] = "str"

#         if data["bank_logo_url"]=='':
#             data["bank_logo_url"] = "str"

#         if data["sqs_qrc_processing_in"]=='':
#             data["sqs_qrc_processing_in"] = "str"

#         if data["sqs_qrc_processing_out"]=='':
#             data["sqs_qrc_processing_out"] = "str"

#         if data["sqs_customer_in"]=='':
#             data["sqs_customer_in"] = "str"

#         if data["sqs_customer_out"]=='':
#             data["sqs_customer_out"] = "str"

#         if data["sqs_transaction_in"]=='':
#             data["sqs_transaction_in"] = "str"

#         if data["sqs_transaction_out"]=='':
#             data["sqs_transaction_out"] = "str"

#         if data["sqs_validation_in"]=='':
#             data["sqs_validation_in"] = "str"

#         if data["sqs_validation_out"]=='':
#             data["sqs_validation_out"] = "str"

#         if data["s3_bucket"]=='':
#             data["s3_bucket"] = "str"


#        # if data["s3_bucket_url"]=='':
#         #    data["s3_bucket_url"] = "str"

#         if data["s3_print_bucket"]=='':
#             data["s3_print_bucket"] = "str"

#         if data["s3_c_exchange_folder"]=='':
#             data["s3_c_exchange_folder"] = "str"

#         if data["s3_c_internal_foder"]=='':
#             data["s3_c_internal_foder"] = "str"

#         requests.patch(settings.DYNAMODB_URL + str(instance.id), json=data, headers={"Content-Type": "application/json"})

# post_save.connect(post_api, sender=Bank)





