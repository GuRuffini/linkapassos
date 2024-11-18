from validate_docbr import CNPJ
from django.core.exceptions import ValidationError

def validate_cnpj(value):
    """
    Validador para CNPJ usando a biblioteca validate-docbr.
    """
    cnpj_validator = CNPJ()
    
    if not cnpj_validator.validate(value):
        raise ValidationError('CNPJ inválido. Certifique-se de que o número está correto.')
    
    if len(value) != 14 or not value.isdigit():
        raise ValidationError('CNPJ deve ter exatamente 14 dígitos numéricos.')
