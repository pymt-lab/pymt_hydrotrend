


cdef extern from "bmi.h":
    ctypedef struct BMI_Model:
        pass

    BMI_Model* register_bmi_hydrotrend(BMI_Model *model)


