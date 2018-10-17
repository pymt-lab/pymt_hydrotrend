


cdef extern from "bmi.h":
    ctypedef struct BMI_Model:
        pass

    BMI_Model* Hydrotrend(BMI_Model *model)

