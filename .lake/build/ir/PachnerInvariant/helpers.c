// Lean compiler output
// Module: PachnerInvariant.helpers
// Imports: public import Init public import PachnerInvariant.descent_property
#include <lean/lean.h>
#if defined(__clang__)
#pragma clang diagnostic ignored "-Wunused-parameter"
#pragma clang diagnostic ignored "-Wunused-label"
#elif defined(__GNUC__) && !defined(__CLANG__)
#pragma GCC diagnostic ignored "-Wunused-parameter"
#pragma GCC diagnostic ignored "-Wunused-label"
#pragma GCC diagnostic ignored "-Wunused-but-set-variable"
#endif
#ifdef __cplusplus
extern "C" {
#endif
lean_object* l_List_lengthTR___redArg(lean_object*);
lean_object* lp_pachner__invariant_PachnerInvariant_tetEq___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_List_foldl___at___00PachnerInvariant_apply__moves_spec__0___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_pachner__invariant_PachnerInvariant_can__apply__pachner23(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
uint8_t l_List_isEmpty___redArg(lean_object*);
lean_object* lp_pachner__invariant_PachnerInvariant_allFaces(lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_can__apply__pachner23___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* l_List_range(lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_List_foldl___at___00PachnerInvariant_apply__moves_spec__0(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
lean_object* lp_pachner__invariant_PachnerInvariant_pachner23(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
uint8_t lean_nat_dec_lt(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_total__simplices(lean_object*);
LEAN_EXPORT uint8_t lp_pachner__invariant_PachnerInvariant_is__valid(lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_can__apply__pachner32___boxed(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_is__valid___boxed(lean_object*);
lean_object* lp_pachner__invariant_PachnerInvariant_allEdges(lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_apply__moves(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT uint8_t lp_pachner__invariant_PachnerInvariant_can__apply__pachner32(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
uint8_t l_List_any___redArg(lean_object*, lean_object*);
lean_object* lean_nat_add(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_total__simplices(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; lean_object* x_4; lean_object* x_5; lean_object* x_6; lean_object* x_7; lean_object* x_8; lean_object* x_9; lean_object* x_10; lean_object* x_11; 
x_2 = lean_ctor_get(x_1, 0);
x_3 = lean_ctor_get(x_1, 1);
lean_inc(x_3);
lean_inc_ref(x_1);
x_4 = lp_pachner__invariant_PachnerInvariant_allEdges(x_1);
x_5 = l_List_lengthTR___redArg(x_4);
lean_dec(x_4);
x_6 = lean_nat_add(x_2, x_5);
lean_dec(x_5);
x_7 = lp_pachner__invariant_PachnerInvariant_allFaces(x_1);
x_8 = l_List_lengthTR___redArg(x_7);
lean_dec(x_7);
x_9 = lean_nat_add(x_6, x_8);
lean_dec(x_8);
lean_dec(x_6);
x_10 = l_List_lengthTR___redArg(x_3);
lean_dec(x_3);
x_11 = lean_nat_add(x_9, x_10);
lean_dec(x_10);
lean_dec(x_9);
return x_11;
}
}
LEAN_EXPORT uint8_t lp_pachner__invariant_PachnerInvariant_is__valid(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; lean_object* x_4; uint8_t x_5; 
x_2 = lean_ctor_get(x_1, 0);
x_3 = lean_ctor_get(x_1, 1);
x_4 = lean_unsigned_to_nat(0u);
x_5 = lean_nat_dec_lt(x_4, x_2);
if (x_5 == 0)
{
return x_5;
}
else
{
uint8_t x_6; 
x_6 = l_List_isEmpty___redArg(x_3);
if (x_6 == 0)
{
return x_5;
}
else
{
uint8_t x_7; 
x_7 = 0;
return x_7;
}
}
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_is__valid___boxed(lean_object* x_1) {
_start:
{
uint8_t x_2; lean_object* x_3; 
x_2 = lp_pachner__invariant_PachnerInvariant_is__valid(x_1);
lean_dec_ref(x_1);
x_3 = lean_box(x_2);
return x_3;
}
}
LEAN_EXPORT uint8_t lp_pachner__invariant_PachnerInvariant_can__apply__pachner23(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4, lean_object* x_5, lean_object* x_6) {
_start:
{
uint8_t x_7; 
x_7 = !lean_is_exclusive(x_1);
if (x_7 == 0)
{
lean_object* x_8; lean_object* x_9; lean_object* x_10; lean_object* x_11; lean_object* x_12; uint8_t x_13; 
x_8 = lean_ctor_get(x_1, 1);
x_9 = lean_ctor_get(x_1, 0);
lean_dec(x_9);
lean_inc(x_4);
lean_ctor_set(x_1, 1, x_5);
lean_ctor_set(x_1, 0, x_4);
lean_inc(x_3);
x_10 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_10, 0, x_3);
lean_ctor_set(x_10, 1, x_1);
lean_inc(x_2);
x_11 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_11, 0, x_2);
lean_ctor_set(x_11, 1, x_10);
x_12 = lean_alloc_closure((void*)(lp_pachner__invariant_PachnerInvariant_tetEq___boxed), 2, 1);
lean_closure_set(x_12, 0, x_11);
lean_inc(x_8);
x_13 = l_List_any___redArg(x_8, x_12);
if (x_13 == 0)
{
lean_dec(x_8);
lean_dec(x_6);
lean_dec(x_4);
lean_dec(x_3);
lean_dec(x_2);
return x_13;
}
else
{
lean_object* x_14; lean_object* x_15; lean_object* x_16; lean_object* x_17; uint8_t x_18; 
x_14 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_14, 0, x_4);
lean_ctor_set(x_14, 1, x_6);
x_15 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_15, 0, x_3);
lean_ctor_set(x_15, 1, x_14);
x_16 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_16, 0, x_2);
lean_ctor_set(x_16, 1, x_15);
x_17 = lean_alloc_closure((void*)(lp_pachner__invariant_PachnerInvariant_tetEq___boxed), 2, 1);
lean_closure_set(x_17, 0, x_16);
x_18 = l_List_any___redArg(x_8, x_17);
return x_18;
}
}
else
{
lean_object* x_19; lean_object* x_20; lean_object* x_21; lean_object* x_22; lean_object* x_23; uint8_t x_24; 
x_19 = lean_ctor_get(x_1, 1);
lean_inc(x_19);
lean_dec(x_1);
lean_inc(x_4);
x_20 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_20, 0, x_4);
lean_ctor_set(x_20, 1, x_5);
lean_inc(x_3);
x_21 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_21, 0, x_3);
lean_ctor_set(x_21, 1, x_20);
lean_inc(x_2);
x_22 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_22, 0, x_2);
lean_ctor_set(x_22, 1, x_21);
x_23 = lean_alloc_closure((void*)(lp_pachner__invariant_PachnerInvariant_tetEq___boxed), 2, 1);
lean_closure_set(x_23, 0, x_22);
lean_inc(x_19);
x_24 = l_List_any___redArg(x_19, x_23);
if (x_24 == 0)
{
lean_dec(x_19);
lean_dec(x_6);
lean_dec(x_4);
lean_dec(x_3);
lean_dec(x_2);
return x_24;
}
else
{
lean_object* x_25; lean_object* x_26; lean_object* x_27; lean_object* x_28; uint8_t x_29; 
x_25 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_25, 0, x_4);
lean_ctor_set(x_25, 1, x_6);
x_26 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_26, 0, x_3);
lean_ctor_set(x_26, 1, x_25);
x_27 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_27, 0, x_2);
lean_ctor_set(x_27, 1, x_26);
x_28 = lean_alloc_closure((void*)(lp_pachner__invariant_PachnerInvariant_tetEq___boxed), 2, 1);
lean_closure_set(x_28, 0, x_27);
x_29 = l_List_any___redArg(x_19, x_28);
return x_29;
}
}
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_can__apply__pachner23___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4, lean_object* x_5, lean_object* x_6) {
_start:
{
uint8_t x_7; lean_object* x_8; 
x_7 = lp_pachner__invariant_PachnerInvariant_can__apply__pachner23(x_1, x_2, x_3, x_4, x_5, x_6);
x_8 = lean_box(x_7);
return x_8;
}
}
LEAN_EXPORT uint8_t lp_pachner__invariant_PachnerInvariant_can__apply__pachner32(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4, lean_object* x_5, lean_object* x_6) {
_start:
{
lean_object* x_7; lean_object* x_8; uint8_t x_9; lean_object* x_16; lean_object* x_17; lean_object* x_18; lean_object* x_19; uint8_t x_20; 
x_7 = lean_ctor_get(x_1, 1);
lean_inc(x_7);
if (lean_is_exclusive(x_1)) {
 lean_ctor_release(x_1, 0);
 lean_ctor_release(x_1, 1);
 x_8 = x_1;
} else {
 lean_dec_ref(x_1);
 x_8 = lean_box(0);
}
lean_inc(x_6);
lean_inc(x_5);
x_16 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_16, 0, x_5);
lean_ctor_set(x_16, 1, x_6);
lean_inc_ref(x_16);
lean_inc(x_3);
x_17 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_17, 0, x_3);
lean_ctor_set(x_17, 1, x_16);
lean_inc(x_2);
x_18 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_18, 0, x_2);
lean_ctor_set(x_18, 1, x_17);
x_19 = lean_alloc_closure((void*)(lp_pachner__invariant_PachnerInvariant_tetEq___boxed), 2, 1);
lean_closure_set(x_19, 0, x_18);
lean_inc(x_7);
x_20 = l_List_any___redArg(x_7, x_19);
if (x_20 == 0)
{
lean_dec_ref(x_16);
lean_dec(x_2);
x_9 = x_20;
goto block_15;
}
else
{
lean_object* x_21; lean_object* x_22; lean_object* x_23; uint8_t x_24; 
lean_inc(x_4);
x_21 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_21, 0, x_4);
lean_ctor_set(x_21, 1, x_16);
x_22 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_22, 0, x_2);
lean_ctor_set(x_22, 1, x_21);
x_23 = lean_alloc_closure((void*)(lp_pachner__invariant_PachnerInvariant_tetEq___boxed), 2, 1);
lean_closure_set(x_23, 0, x_22);
lean_inc(x_7);
x_24 = l_List_any___redArg(x_7, x_23);
x_9 = x_24;
goto block_15;
}
block_15:
{
if (x_9 == 0)
{
lean_dec(x_8);
lean_dec(x_7);
lean_dec(x_6);
lean_dec(x_5);
lean_dec(x_4);
lean_dec(x_3);
return x_9;
}
else
{
lean_object* x_10; lean_object* x_11; lean_object* x_12; lean_object* x_13; uint8_t x_14; 
if (lean_is_scalar(x_8)) {
 x_10 = lean_alloc_ctor(0, 2, 0);
} else {
 x_10 = x_8;
}
lean_ctor_set(x_10, 0, x_5);
lean_ctor_set(x_10, 1, x_6);
x_11 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_11, 0, x_4);
lean_ctor_set(x_11, 1, x_10);
x_12 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_12, 0, x_3);
lean_ctor_set(x_12, 1, x_11);
x_13 = lean_alloc_closure((void*)(lp_pachner__invariant_PachnerInvariant_tetEq___boxed), 2, 1);
lean_closure_set(x_13, 0, x_12);
x_14 = l_List_any___redArg(x_7, x_13);
return x_14;
}
}
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_can__apply__pachner32___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4, lean_object* x_5, lean_object* x_6) {
_start:
{
uint8_t x_7; lean_object* x_8; 
x_7 = lp_pachner__invariant_PachnerInvariant_can__apply__pachner32(x_1, x_2, x_3, x_4, x_5, x_6);
x_8 = lean_box(x_7);
return x_8;
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_List_foldl___at___00PachnerInvariant_apply__moves_spec__0(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4, lean_object* x_5) {
_start:
{
if (lean_obj_tag(x_5) == 0)
{
lean_dec(x_3);
lean_dec(x_2);
lean_dec(x_1);
return x_4;
}
else
{
lean_object* x_6; lean_object* x_7; lean_object* x_8; lean_object* x_9; lean_object* x_10; lean_object* x_11; 
x_6 = lean_ctor_get(x_5, 1);
x_7 = lean_ctor_get(x_4, 1);
x_8 = l_List_lengthTR___redArg(x_7);
x_9 = lean_unsigned_to_nat(1u);
x_10 = lean_nat_add(x_8, x_9);
lean_inc(x_3);
lean_inc(x_2);
lean_inc(x_1);
x_11 = lp_pachner__invariant_PachnerInvariant_pachner23(x_4, x_1, x_2, x_3, x_8, x_10);
x_4 = x_11;
x_5 = x_6;
goto _start;
}
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_List_foldl___at___00PachnerInvariant_apply__moves_spec__0___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4, lean_object* x_5) {
_start:
{
lean_object* x_6; 
x_6 = lp_pachner__invariant_List_foldl___at___00PachnerInvariant_apply__moves_spec__0(x_1, x_2, x_3, x_4, x_5);
lean_dec(x_5);
return x_6;
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_apply__moves(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4, lean_object* x_5) {
_start:
{
lean_object* x_6; lean_object* x_7; 
x_6 = l_List_range(x_5);
x_7 = lp_pachner__invariant_List_foldl___at___00PachnerInvariant_apply__moves_spec__0(x_2, x_3, x_4, x_1, x_6);
lean_dec(x_6);
return x_7;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_pachner__invariant_PachnerInvariant_descent__property(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_pachner__invariant_PachnerInvariant_helpers(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_pachner__invariant_PachnerInvariant_descent__property(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
