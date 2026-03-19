// Lean compiler output
// Module: PachnerInvariant.lambda_optimization
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
static lean_object* lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__2;
lean_object* l_List_lengthTR___redArg(lean_object*);
lean_object* lean_mk_empty_array_with_capacity(lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_theta__with__lam___boxed(lean_object*, lean_object*);
uint8_t lp_pachner__invariant_PachnerInvariant_isImproving(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
static lean_object* lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__0;
uint8_t l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_countImprovingMoves(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_List_filterTR_loop___at___00PachnerInvariant_tetPairToMove_spec__0___boxed(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant___private_Init_Data_List_Impl_0__List_flatMapTR_go___at___00PachnerInvariant_findImprovingMove_spec__1(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_findImprovingMove(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_sharedVerts(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_optimize__lam(lean_object*);
lean_object* l_List_foldl___at___00Array_appendList_spec__0___redArg(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_findImprovingMove___lam__0(lean_object*, lean_object*, lean_object*);
static lean_object* lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__3;
static lean_object* lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__1;
lean_object* l_List_findSome_x3f___redArg(lean_object*, lean_object*);
lean_object* lean_array_to_list(lean_object*);
lean_object* lp_pachner__invariant_PachnerInvariant_tetToVerts(lean_object*);
static lean_object* lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__4;
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_optimize__lam__after__move(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_List_mapTR_loop___at___00PachnerInvariant_findImprovingMove_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_List_foldl___at___00PachnerInvariant_optimize__lam_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_List_filterTR_loop___at___00PachnerInvariant_sharedVerts_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_tetPairToMove(lean_object*, lean_object*);
lean_object* lp_pachner__invariant_PachnerInvariant_pachner23(lean_object*, lean_object*, lean_object*, lean_object*, lean_object*, lean_object*);
uint8_t lean_nat_dec_eq(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_greedyImprove(lean_object*, lean_object*, lean_object*);
uint8_t lean_nat_dec_lt(lean_object*, lean_object*);
lean_object* l_List_reverse___redArg(lean_object*);
lean_object* lean_nat_sub(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_List_countP_go___at___00PachnerInvariant_countImprovingMoves_spec__0(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_List_foldl___at___00PachnerInvariant_optimize__lam_spec__0___boxed(lean_object*, lean_object*, lean_object*);
lean_object* lp_pachner__invariant_PachnerInvariant_theta(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_countImprovingMoves___boxed(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_theta__with__lam(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_findImprovingMove___lam__0___boxed(lean_object*, lean_object*, lean_object*);
static lean_object* lp_pachner__invariant_PachnerInvariant_findImprovingMove___closed__0;
lean_object* lean_nat_add(lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_List_filterTR_loop___at___00PachnerInvariant_tetPairToMove_spec__0(lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_List_countP_go___at___00PachnerInvariant_countImprovingMoves_spec__0___boxed(lean_object*, lean_object*, lean_object*, lean_object*);
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_theta__with__lam(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lp_pachner__invariant_PachnerInvariant_theta(x_1, x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_theta__with__lam___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lp_pachner__invariant_PachnerInvariant_theta__with__lam(x_1, x_2);
lean_dec(x_2);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_List_foldl___at___00PachnerInvariant_optimize__lam_spec__0(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
if (lean_obj_tag(x_3) == 0)
{
lean_dec_ref(x_1);
lean_inc(x_2);
return x_2;
}
else
{
lean_object* x_4; lean_object* x_5; lean_object* x_6; lean_object* x_7; uint8_t x_8; 
x_4 = lean_ctor_get(x_3, 0);
x_5 = lean_ctor_get(x_3, 1);
lean_inc_ref(x_1);
x_6 = lp_pachner__invariant_PachnerInvariant_theta(x_1, x_4);
lean_inc_ref(x_1);
x_7 = lp_pachner__invariant_PachnerInvariant_theta(x_1, x_2);
x_8 = lean_nat_dec_lt(x_6, x_7);
lean_dec(x_7);
lean_dec(x_6);
if (x_8 == 0)
{
x_3 = x_5;
goto _start;
}
else
{
x_2 = x_4;
x_3 = x_5;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_List_foldl___at___00PachnerInvariant_optimize__lam_spec__0___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; 
x_4 = lp_pachner__invariant_List_foldl___at___00PachnerInvariant_optimize__lam_spec__0(x_1, x_2, x_3);
lean_dec(x_3);
lean_dec(x_2);
return x_4;
}
}
static lean_object* _init_lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__0() {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = lean_box(0);
x_2 = lean_unsigned_to_nat(5u);
x_3 = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(x_3, 0, x_2);
lean_ctor_set(x_3, 1, x_1);
return x_3;
}
}
static lean_object* _init_lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__1() {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__0;
x_2 = lean_unsigned_to_nat(4u);
x_3 = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(x_3, 0, x_2);
lean_ctor_set(x_3, 1, x_1);
return x_3;
}
}
static lean_object* _init_lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__2() {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__1;
x_2 = lean_unsigned_to_nat(3u);
x_3 = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(x_3, 0, x_2);
lean_ctor_set(x_3, 1, x_1);
return x_3;
}
}
static lean_object* _init_lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__3() {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__2;
x_2 = lean_unsigned_to_nat(2u);
x_3 = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(x_3, 0, x_2);
lean_ctor_set(x_3, 1, x_1);
return x_3;
}
}
static lean_object* _init_lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__4() {
_start:
{
lean_object* x_1; lean_object* x_2; lean_object* x_3; 
x_1 = lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__3;
x_2 = lean_unsigned_to_nat(1u);
x_3 = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(x_3, 0, x_2);
lean_ctor_set(x_3, 1, x_1);
return x_3;
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_optimize__lam(lean_object* x_1) {
_start:
{
lean_object* x_2; lean_object* x_3; lean_object* x_4; 
x_2 = lean_unsigned_to_nat(1u);
x_3 = lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__4;
x_4 = lp_pachner__invariant_List_foldl___at___00PachnerInvariant_optimize__lam_spec__0(x_1, x_2, x_3);
return x_4;
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_optimize__lam__after__move(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4, lean_object* x_5, lean_object* x_6) {
_start:
{
lean_object* x_7; lean_object* x_8; 
x_7 = lp_pachner__invariant_PachnerInvariant_pachner23(x_1, x_2, x_3, x_4, x_5, x_6);
x_8 = lp_pachner__invariant_PachnerInvariant_optimize__lam(x_7);
return x_8;
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_List_filterTR_loop___at___00PachnerInvariant_sharedVerts_spec__0(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
if (lean_obj_tag(x_2) == 0)
{
lean_object* x_4; 
lean_dec_ref(x_1);
x_4 = l_List_reverse___redArg(x_3);
return x_4;
}
else
{
uint8_t x_5; 
x_5 = !lean_is_exclusive(x_2);
if (x_5 == 0)
{
lean_object* x_6; lean_object* x_7; lean_object* x_8; uint8_t x_9; 
x_6 = lean_ctor_get(x_2, 0);
x_7 = lean_ctor_get(x_2, 1);
lean_inc_ref(x_1);
x_8 = lp_pachner__invariant_PachnerInvariant_tetToVerts(x_1);
x_9 = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(x_6, x_8);
lean_dec(x_8);
if (x_9 == 0)
{
lean_free_object(x_2);
lean_dec(x_6);
x_2 = x_7;
goto _start;
}
else
{
lean_ctor_set(x_2, 1, x_3);
{
lean_object* _tmp_1 = x_7;
lean_object* _tmp_2 = x_2;
x_2 = _tmp_1;
x_3 = _tmp_2;
}
goto _start;
}
}
else
{
lean_object* x_12; lean_object* x_13; lean_object* x_14; uint8_t x_15; 
x_12 = lean_ctor_get(x_2, 0);
x_13 = lean_ctor_get(x_2, 1);
lean_inc(x_13);
lean_inc(x_12);
lean_dec(x_2);
lean_inc_ref(x_1);
x_14 = lp_pachner__invariant_PachnerInvariant_tetToVerts(x_1);
x_15 = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(x_12, x_14);
lean_dec(x_14);
if (x_15 == 0)
{
lean_dec(x_12);
x_2 = x_13;
goto _start;
}
else
{
lean_object* x_17; 
x_17 = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(x_17, 0, x_12);
lean_ctor_set(x_17, 1, x_3);
x_2 = x_13;
x_3 = x_17;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_sharedVerts(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; lean_object* x_4; lean_object* x_5; 
x_3 = lp_pachner__invariant_PachnerInvariant_tetToVerts(x_1);
x_4 = lean_box(0);
x_5 = lp_pachner__invariant_List_filterTR_loop___at___00PachnerInvariant_sharedVerts_spec__0(x_2, x_3, x_4);
return x_5;
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_List_filterTR_loop___at___00PachnerInvariant_tetPairToMove_spec__0(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
if (lean_obj_tag(x_2) == 0)
{
lean_object* x_4; 
x_4 = l_List_reverse___redArg(x_3);
return x_4;
}
else
{
uint8_t x_5; 
x_5 = !lean_is_exclusive(x_2);
if (x_5 == 0)
{
lean_object* x_6; lean_object* x_7; uint8_t x_8; 
x_6 = lean_ctor_get(x_2, 0);
x_7 = lean_ctor_get(x_2, 1);
x_8 = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(x_6, x_1);
if (x_8 == 0)
{
lean_ctor_set(x_2, 1, x_3);
{
lean_object* _tmp_1 = x_7;
lean_object* _tmp_2 = x_2;
x_2 = _tmp_1;
x_3 = _tmp_2;
}
goto _start;
}
else
{
lean_free_object(x_2);
lean_dec(x_6);
x_2 = x_7;
goto _start;
}
}
else
{
lean_object* x_11; lean_object* x_12; uint8_t x_13; 
x_11 = lean_ctor_get(x_2, 0);
x_12 = lean_ctor_get(x_2, 1);
lean_inc(x_12);
lean_inc(x_11);
lean_dec(x_2);
x_13 = l_List_elem___at___00Lean_Meta_Occurrences_contains_spec__0(x_11, x_1);
if (x_13 == 0)
{
lean_object* x_14; 
x_14 = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(x_14, 0, x_11);
lean_ctor_set(x_14, 1, x_3);
x_2 = x_12;
x_3 = x_14;
goto _start;
}
else
{
lean_dec(x_11);
x_2 = x_12;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_List_filterTR_loop___at___00PachnerInvariant_tetPairToMove_spec__0___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; 
x_4 = lp_pachner__invariant_List_filterTR_loop___at___00PachnerInvariant_tetPairToMove_spec__0(x_1, x_2, x_3);
lean_dec(x_1);
return x_4;
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_tetPairToMove(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; lean_object* x_4; lean_object* x_5; uint8_t x_6; 
lean_inc_ref(x_2);
lean_inc_ref(x_1);
x_3 = lp_pachner__invariant_PachnerInvariant_sharedVerts(x_1, x_2);
x_4 = l_List_lengthTR___redArg(x_3);
x_5 = lean_unsigned_to_nat(3u);
x_6 = lean_nat_dec_eq(x_4, x_5);
lean_dec(x_4);
if (x_6 == 0)
{
lean_object* x_7; 
lean_dec(x_3);
lean_dec_ref(x_2);
lean_dec_ref(x_1);
x_7 = lean_box(0);
return x_7;
}
else
{
if (lean_obj_tag(x_3) == 1)
{
lean_object* x_8; 
x_8 = lean_ctor_get(x_3, 1);
lean_inc(x_8);
if (lean_obj_tag(x_8) == 1)
{
lean_object* x_9; 
x_9 = lean_ctor_get(x_8, 1);
lean_inc(x_9);
if (lean_obj_tag(x_9) == 1)
{
lean_object* x_10; 
x_10 = lean_ctor_get(x_9, 1);
if (lean_obj_tag(x_10) == 0)
{
lean_object* x_11; uint8_t x_12; 
x_11 = lean_ctor_get(x_3, 0);
lean_inc(x_11);
x_12 = !lean_is_exclusive(x_8);
if (x_12 == 0)
{
lean_object* x_13; lean_object* x_14; uint8_t x_15; 
x_13 = lean_ctor_get(x_8, 0);
x_14 = lean_ctor_get(x_8, 1);
lean_dec(x_14);
x_15 = !lean_is_exclusive(x_9);
if (x_15 == 0)
{
lean_object* x_16; lean_object* x_17; lean_object* x_18; lean_object* x_19; lean_object* x_20; 
x_16 = lean_ctor_get(x_9, 0);
x_17 = lean_ctor_get(x_9, 1);
lean_dec(x_17);
x_18 = lp_pachner__invariant_PachnerInvariant_tetToVerts(x_1);
x_19 = lean_box(0);
x_20 = lp_pachner__invariant_List_filterTR_loop___at___00PachnerInvariant_tetPairToMove_spec__0(x_3, x_18, x_19);
if (lean_obj_tag(x_20) == 1)
{
lean_object* x_21; 
x_21 = lean_ctor_get(x_20, 1);
lean_inc(x_21);
if (lean_obj_tag(x_21) == 0)
{
uint8_t x_22; 
x_22 = !lean_is_exclusive(x_20);
if (x_22 == 0)
{
lean_object* x_23; lean_object* x_24; lean_object* x_25; lean_object* x_26; 
x_23 = lean_ctor_get(x_20, 0);
x_24 = lean_ctor_get(x_20, 1);
lean_dec(x_24);
x_25 = lp_pachner__invariant_PachnerInvariant_tetToVerts(x_2);
x_26 = lp_pachner__invariant_List_filterTR_loop___at___00PachnerInvariant_tetPairToMove_spec__0(x_3, x_25, x_21);
lean_dec_ref(x_3);
if (lean_obj_tag(x_26) == 1)
{
lean_object* x_27; 
x_27 = lean_ctor_get(x_26, 1);
lean_inc(x_27);
if (lean_obj_tag(x_27) == 0)
{
uint8_t x_28; 
x_28 = !lean_is_exclusive(x_26);
if (x_28 == 0)
{
lean_object* x_29; lean_object* x_30; uint8_t x_31; 
x_29 = lean_ctor_get(x_26, 0);
x_30 = lean_ctor_get(x_26, 1);
lean_dec(x_30);
x_31 = lean_nat_dec_eq(x_23, x_29);
if (x_31 == 0)
{
if (x_6 == 0)
{
lean_object* x_32; 
lean_free_object(x_26);
lean_dec(x_29);
lean_free_object(x_20);
lean_dec(x_23);
lean_free_object(x_9);
lean_dec(x_16);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
x_32 = lean_box(0);
return x_32;
}
else
{
lean_object* x_33; 
lean_ctor_set_tag(x_26, 0);
lean_ctor_set(x_26, 1, x_29);
lean_ctor_set(x_26, 0, x_23);
lean_ctor_set_tag(x_20, 0);
lean_ctor_set(x_20, 1, x_26);
lean_ctor_set(x_20, 0, x_16);
lean_ctor_set_tag(x_9, 0);
lean_ctor_set(x_9, 1, x_20);
lean_ctor_set(x_9, 0, x_13);
lean_ctor_set_tag(x_8, 0);
lean_ctor_set(x_8, 0, x_11);
x_33 = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(x_33, 0, x_8);
return x_33;
}
}
else
{
lean_object* x_34; 
lean_free_object(x_26);
lean_dec(x_29);
lean_free_object(x_20);
lean_dec(x_23);
lean_free_object(x_9);
lean_dec(x_16);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
x_34 = lean_box(0);
return x_34;
}
}
else
{
lean_object* x_35; uint8_t x_36; 
x_35 = lean_ctor_get(x_26, 0);
lean_inc(x_35);
lean_dec(x_26);
x_36 = lean_nat_dec_eq(x_23, x_35);
if (x_36 == 0)
{
if (x_6 == 0)
{
lean_object* x_37; 
lean_dec(x_35);
lean_free_object(x_20);
lean_dec(x_23);
lean_free_object(x_9);
lean_dec(x_16);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
x_37 = lean_box(0);
return x_37;
}
else
{
lean_object* x_38; lean_object* x_39; 
x_38 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_38, 0, x_23);
lean_ctor_set(x_38, 1, x_35);
lean_ctor_set_tag(x_20, 0);
lean_ctor_set(x_20, 1, x_38);
lean_ctor_set(x_20, 0, x_16);
lean_ctor_set_tag(x_9, 0);
lean_ctor_set(x_9, 1, x_20);
lean_ctor_set(x_9, 0, x_13);
lean_ctor_set_tag(x_8, 0);
lean_ctor_set(x_8, 0, x_11);
x_39 = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(x_39, 0, x_8);
return x_39;
}
}
else
{
lean_object* x_40; 
lean_dec(x_35);
lean_free_object(x_20);
lean_dec(x_23);
lean_free_object(x_9);
lean_dec(x_16);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
x_40 = lean_box(0);
return x_40;
}
}
}
else
{
lean_object* x_41; 
lean_dec(x_27);
lean_dec_ref(x_26);
lean_free_object(x_20);
lean_dec(x_23);
lean_free_object(x_9);
lean_dec(x_16);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
x_41 = lean_box(0);
return x_41;
}
}
else
{
lean_object* x_42; 
lean_dec(x_26);
lean_free_object(x_20);
lean_dec(x_23);
lean_free_object(x_9);
lean_dec(x_16);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
x_42 = lean_box(0);
return x_42;
}
}
else
{
lean_object* x_43; lean_object* x_44; lean_object* x_45; 
x_43 = lean_ctor_get(x_20, 0);
lean_inc(x_43);
lean_dec(x_20);
x_44 = lp_pachner__invariant_PachnerInvariant_tetToVerts(x_2);
x_45 = lp_pachner__invariant_List_filterTR_loop___at___00PachnerInvariant_tetPairToMove_spec__0(x_3, x_44, x_21);
lean_dec_ref(x_3);
if (lean_obj_tag(x_45) == 1)
{
lean_object* x_46; 
x_46 = lean_ctor_get(x_45, 1);
lean_inc(x_46);
if (lean_obj_tag(x_46) == 0)
{
lean_object* x_47; lean_object* x_48; uint8_t x_49; 
x_47 = lean_ctor_get(x_45, 0);
lean_inc(x_47);
if (lean_is_exclusive(x_45)) {
 lean_ctor_release(x_45, 0);
 lean_ctor_release(x_45, 1);
 x_48 = x_45;
} else {
 lean_dec_ref(x_45);
 x_48 = lean_box(0);
}
x_49 = lean_nat_dec_eq(x_43, x_47);
if (x_49 == 0)
{
if (x_6 == 0)
{
lean_object* x_50; 
lean_dec(x_48);
lean_dec(x_47);
lean_dec(x_43);
lean_free_object(x_9);
lean_dec(x_16);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
x_50 = lean_box(0);
return x_50;
}
else
{
lean_object* x_51; lean_object* x_52; lean_object* x_53; 
if (lean_is_scalar(x_48)) {
 x_51 = lean_alloc_ctor(0, 2, 0);
} else {
 x_51 = x_48;
 lean_ctor_set_tag(x_51, 0);
}
lean_ctor_set(x_51, 0, x_43);
lean_ctor_set(x_51, 1, x_47);
x_52 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_52, 0, x_16);
lean_ctor_set(x_52, 1, x_51);
lean_ctor_set_tag(x_9, 0);
lean_ctor_set(x_9, 1, x_52);
lean_ctor_set(x_9, 0, x_13);
lean_ctor_set_tag(x_8, 0);
lean_ctor_set(x_8, 0, x_11);
x_53 = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(x_53, 0, x_8);
return x_53;
}
}
else
{
lean_object* x_54; 
lean_dec(x_48);
lean_dec(x_47);
lean_dec(x_43);
lean_free_object(x_9);
lean_dec(x_16);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
x_54 = lean_box(0);
return x_54;
}
}
else
{
lean_object* x_55; 
lean_dec(x_46);
lean_dec_ref(x_45);
lean_dec(x_43);
lean_free_object(x_9);
lean_dec(x_16);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
x_55 = lean_box(0);
return x_55;
}
}
else
{
lean_object* x_56; 
lean_dec(x_45);
lean_dec(x_43);
lean_free_object(x_9);
lean_dec(x_16);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
x_56 = lean_box(0);
return x_56;
}
}
}
else
{
lean_object* x_57; 
lean_dec(x_21);
lean_dec_ref(x_20);
lean_free_object(x_9);
lean_dec(x_16);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
lean_dec_ref(x_3);
lean_dec_ref(x_2);
x_57 = lean_box(0);
return x_57;
}
}
else
{
lean_object* x_58; 
lean_dec(x_20);
lean_free_object(x_9);
lean_dec(x_16);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
lean_dec_ref(x_3);
lean_dec_ref(x_2);
x_58 = lean_box(0);
return x_58;
}
}
else
{
lean_object* x_59; lean_object* x_60; lean_object* x_61; lean_object* x_62; 
x_59 = lean_ctor_get(x_9, 0);
lean_inc(x_59);
lean_dec(x_9);
x_60 = lp_pachner__invariant_PachnerInvariant_tetToVerts(x_1);
x_61 = lean_box(0);
x_62 = lp_pachner__invariant_List_filterTR_loop___at___00PachnerInvariant_tetPairToMove_spec__0(x_3, x_60, x_61);
if (lean_obj_tag(x_62) == 1)
{
lean_object* x_63; 
x_63 = lean_ctor_get(x_62, 1);
lean_inc(x_63);
if (lean_obj_tag(x_63) == 0)
{
lean_object* x_64; lean_object* x_65; lean_object* x_66; lean_object* x_67; 
x_64 = lean_ctor_get(x_62, 0);
lean_inc(x_64);
if (lean_is_exclusive(x_62)) {
 lean_ctor_release(x_62, 0);
 lean_ctor_release(x_62, 1);
 x_65 = x_62;
} else {
 lean_dec_ref(x_62);
 x_65 = lean_box(0);
}
x_66 = lp_pachner__invariant_PachnerInvariant_tetToVerts(x_2);
x_67 = lp_pachner__invariant_List_filterTR_loop___at___00PachnerInvariant_tetPairToMove_spec__0(x_3, x_66, x_63);
lean_dec_ref(x_3);
if (lean_obj_tag(x_67) == 1)
{
lean_object* x_68; 
x_68 = lean_ctor_get(x_67, 1);
lean_inc(x_68);
if (lean_obj_tag(x_68) == 0)
{
lean_object* x_69; lean_object* x_70; uint8_t x_71; 
x_69 = lean_ctor_get(x_67, 0);
lean_inc(x_69);
if (lean_is_exclusive(x_67)) {
 lean_ctor_release(x_67, 0);
 lean_ctor_release(x_67, 1);
 x_70 = x_67;
} else {
 lean_dec_ref(x_67);
 x_70 = lean_box(0);
}
x_71 = lean_nat_dec_eq(x_64, x_69);
if (x_71 == 0)
{
if (x_6 == 0)
{
lean_object* x_72; 
lean_dec(x_70);
lean_dec(x_69);
lean_dec(x_65);
lean_dec(x_64);
lean_dec(x_59);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
x_72 = lean_box(0);
return x_72;
}
else
{
lean_object* x_73; lean_object* x_74; lean_object* x_75; lean_object* x_76; 
if (lean_is_scalar(x_70)) {
 x_73 = lean_alloc_ctor(0, 2, 0);
} else {
 x_73 = x_70;
 lean_ctor_set_tag(x_73, 0);
}
lean_ctor_set(x_73, 0, x_64);
lean_ctor_set(x_73, 1, x_69);
if (lean_is_scalar(x_65)) {
 x_74 = lean_alloc_ctor(0, 2, 0);
} else {
 x_74 = x_65;
 lean_ctor_set_tag(x_74, 0);
}
lean_ctor_set(x_74, 0, x_59);
lean_ctor_set(x_74, 1, x_73);
x_75 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_75, 0, x_13);
lean_ctor_set(x_75, 1, x_74);
lean_ctor_set_tag(x_8, 0);
lean_ctor_set(x_8, 1, x_75);
lean_ctor_set(x_8, 0, x_11);
x_76 = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(x_76, 0, x_8);
return x_76;
}
}
else
{
lean_object* x_77; 
lean_dec(x_70);
lean_dec(x_69);
lean_dec(x_65);
lean_dec(x_64);
lean_dec(x_59);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
x_77 = lean_box(0);
return x_77;
}
}
else
{
lean_object* x_78; 
lean_dec(x_68);
lean_dec_ref(x_67);
lean_dec(x_65);
lean_dec(x_64);
lean_dec(x_59);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
x_78 = lean_box(0);
return x_78;
}
}
else
{
lean_object* x_79; 
lean_dec(x_67);
lean_dec(x_65);
lean_dec(x_64);
lean_dec(x_59);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
x_79 = lean_box(0);
return x_79;
}
}
else
{
lean_object* x_80; 
lean_dec(x_63);
lean_dec_ref(x_62);
lean_dec(x_59);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
lean_dec_ref(x_3);
lean_dec_ref(x_2);
x_80 = lean_box(0);
return x_80;
}
}
else
{
lean_object* x_81; 
lean_dec(x_62);
lean_dec(x_59);
lean_free_object(x_8);
lean_dec(x_13);
lean_dec(x_11);
lean_dec_ref(x_3);
lean_dec_ref(x_2);
x_81 = lean_box(0);
return x_81;
}
}
}
else
{
lean_object* x_82; lean_object* x_83; lean_object* x_84; lean_object* x_85; lean_object* x_86; lean_object* x_87; 
x_82 = lean_ctor_get(x_8, 0);
lean_inc(x_82);
lean_dec(x_8);
x_83 = lean_ctor_get(x_9, 0);
lean_inc(x_83);
if (lean_is_exclusive(x_9)) {
 lean_ctor_release(x_9, 0);
 lean_ctor_release(x_9, 1);
 x_84 = x_9;
} else {
 lean_dec_ref(x_9);
 x_84 = lean_box(0);
}
x_85 = lp_pachner__invariant_PachnerInvariant_tetToVerts(x_1);
x_86 = lean_box(0);
x_87 = lp_pachner__invariant_List_filterTR_loop___at___00PachnerInvariant_tetPairToMove_spec__0(x_3, x_85, x_86);
if (lean_obj_tag(x_87) == 1)
{
lean_object* x_88; 
x_88 = lean_ctor_get(x_87, 1);
lean_inc(x_88);
if (lean_obj_tag(x_88) == 0)
{
lean_object* x_89; lean_object* x_90; lean_object* x_91; lean_object* x_92; 
x_89 = lean_ctor_get(x_87, 0);
lean_inc(x_89);
if (lean_is_exclusive(x_87)) {
 lean_ctor_release(x_87, 0);
 lean_ctor_release(x_87, 1);
 x_90 = x_87;
} else {
 lean_dec_ref(x_87);
 x_90 = lean_box(0);
}
x_91 = lp_pachner__invariant_PachnerInvariant_tetToVerts(x_2);
x_92 = lp_pachner__invariant_List_filterTR_loop___at___00PachnerInvariant_tetPairToMove_spec__0(x_3, x_91, x_88);
lean_dec_ref(x_3);
if (lean_obj_tag(x_92) == 1)
{
lean_object* x_93; 
x_93 = lean_ctor_get(x_92, 1);
lean_inc(x_93);
if (lean_obj_tag(x_93) == 0)
{
lean_object* x_94; lean_object* x_95; uint8_t x_96; 
x_94 = lean_ctor_get(x_92, 0);
lean_inc(x_94);
if (lean_is_exclusive(x_92)) {
 lean_ctor_release(x_92, 0);
 lean_ctor_release(x_92, 1);
 x_95 = x_92;
} else {
 lean_dec_ref(x_92);
 x_95 = lean_box(0);
}
x_96 = lean_nat_dec_eq(x_89, x_94);
if (x_96 == 0)
{
if (x_6 == 0)
{
lean_object* x_97; 
lean_dec(x_95);
lean_dec(x_94);
lean_dec(x_90);
lean_dec(x_89);
lean_dec(x_84);
lean_dec(x_83);
lean_dec(x_82);
lean_dec(x_11);
x_97 = lean_box(0);
return x_97;
}
else
{
lean_object* x_98; lean_object* x_99; lean_object* x_100; lean_object* x_101; lean_object* x_102; 
if (lean_is_scalar(x_95)) {
 x_98 = lean_alloc_ctor(0, 2, 0);
} else {
 x_98 = x_95;
 lean_ctor_set_tag(x_98, 0);
}
lean_ctor_set(x_98, 0, x_89);
lean_ctor_set(x_98, 1, x_94);
if (lean_is_scalar(x_90)) {
 x_99 = lean_alloc_ctor(0, 2, 0);
} else {
 x_99 = x_90;
 lean_ctor_set_tag(x_99, 0);
}
lean_ctor_set(x_99, 0, x_83);
lean_ctor_set(x_99, 1, x_98);
if (lean_is_scalar(x_84)) {
 x_100 = lean_alloc_ctor(0, 2, 0);
} else {
 x_100 = x_84;
 lean_ctor_set_tag(x_100, 0);
}
lean_ctor_set(x_100, 0, x_82);
lean_ctor_set(x_100, 1, x_99);
x_101 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_101, 0, x_11);
lean_ctor_set(x_101, 1, x_100);
x_102 = lean_alloc_ctor(1, 1, 0);
lean_ctor_set(x_102, 0, x_101);
return x_102;
}
}
else
{
lean_object* x_103; 
lean_dec(x_95);
lean_dec(x_94);
lean_dec(x_90);
lean_dec(x_89);
lean_dec(x_84);
lean_dec(x_83);
lean_dec(x_82);
lean_dec(x_11);
x_103 = lean_box(0);
return x_103;
}
}
else
{
lean_object* x_104; 
lean_dec(x_93);
lean_dec_ref(x_92);
lean_dec(x_90);
lean_dec(x_89);
lean_dec(x_84);
lean_dec(x_83);
lean_dec(x_82);
lean_dec(x_11);
x_104 = lean_box(0);
return x_104;
}
}
else
{
lean_object* x_105; 
lean_dec(x_92);
lean_dec(x_90);
lean_dec(x_89);
lean_dec(x_84);
lean_dec(x_83);
lean_dec(x_82);
lean_dec(x_11);
x_105 = lean_box(0);
return x_105;
}
}
else
{
lean_object* x_106; 
lean_dec(x_88);
lean_dec_ref(x_87);
lean_dec(x_84);
lean_dec(x_83);
lean_dec(x_82);
lean_dec(x_11);
lean_dec_ref(x_3);
lean_dec_ref(x_2);
x_106 = lean_box(0);
return x_106;
}
}
else
{
lean_object* x_107; 
lean_dec(x_87);
lean_dec(x_84);
lean_dec(x_83);
lean_dec(x_82);
lean_dec(x_11);
lean_dec_ref(x_3);
lean_dec_ref(x_2);
x_107 = lean_box(0);
return x_107;
}
}
}
else
{
lean_object* x_108; 
lean_dec_ref(x_9);
lean_dec_ref(x_8);
lean_dec_ref(x_3);
lean_dec_ref(x_2);
lean_dec_ref(x_1);
x_108 = lean_box(0);
return x_108;
}
}
else
{
lean_object* x_109; 
lean_dec(x_9);
lean_dec_ref(x_8);
lean_dec_ref(x_3);
lean_dec_ref(x_2);
lean_dec_ref(x_1);
x_109 = lean_box(0);
return x_109;
}
}
else
{
lean_object* x_110; 
lean_dec(x_8);
lean_dec_ref(x_3);
lean_dec_ref(x_2);
lean_dec_ref(x_1);
x_110 = lean_box(0);
return x_110;
}
}
else
{
lean_object* x_111; 
lean_dec(x_3);
lean_dec_ref(x_2);
lean_dec_ref(x_1);
x_111 = lean_box(0);
return x_111;
}
}
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_findImprovingMove___lam__0(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; lean_object* x_5; lean_object* x_6; 
x_4 = lean_ctor_get(x_3, 0);
lean_inc(x_4);
x_5 = lean_ctor_get(x_3, 1);
lean_inc(x_5);
lean_dec_ref(x_3);
x_6 = lp_pachner__invariant_PachnerInvariant_tetPairToMove(x_4, x_5);
if (lean_obj_tag(x_6) == 0)
{
lean_dec_ref(x_1);
return x_6;
}
else
{
lean_object* x_7; lean_object* x_8; lean_object* x_9; lean_object* x_10; lean_object* x_11; lean_object* x_12; lean_object* x_13; lean_object* x_14; lean_object* x_15; uint8_t x_16; 
x_7 = lean_ctor_get(x_6, 0);
lean_inc(x_7);
x_8 = lean_ctor_get(x_7, 1);
lean_inc(x_8);
x_9 = lean_ctor_get(x_8, 1);
lean_inc(x_9);
x_10 = lean_ctor_get(x_9, 1);
lean_inc(x_10);
x_11 = lean_ctor_get(x_7, 0);
lean_inc(x_11);
lean_dec(x_7);
x_12 = lean_ctor_get(x_8, 0);
lean_inc(x_12);
lean_dec(x_8);
x_13 = lean_ctor_get(x_9, 0);
lean_inc(x_13);
lean_dec(x_9);
x_14 = lean_ctor_get(x_10, 0);
lean_inc(x_14);
x_15 = lean_ctor_get(x_10, 1);
lean_inc(x_15);
lean_dec(x_10);
x_16 = lp_pachner__invariant_PachnerInvariant_isImproving(x_1, x_11, x_12, x_13, x_14, x_15, x_2);
if (x_16 == 0)
{
lean_object* x_17; 
lean_dec_ref(x_6);
x_17 = lean_box(0);
return x_17;
}
else
{
return x_6;
}
}
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_findImprovingMove___lam__0___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; 
x_4 = lp_pachner__invariant_PachnerInvariant_findImprovingMove___lam__0(x_1, x_2, x_3);
lean_dec(x_2);
return x_4;
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_List_mapTR_loop___at___00PachnerInvariant_findImprovingMove_spec__0(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
if (lean_obj_tag(x_2) == 0)
{
lean_object* x_4; 
lean_dec_ref(x_1);
x_4 = l_List_reverse___redArg(x_3);
return x_4;
}
else
{
uint8_t x_5; 
x_5 = !lean_is_exclusive(x_2);
if (x_5 == 0)
{
lean_object* x_6; lean_object* x_7; lean_object* x_8; 
x_6 = lean_ctor_get(x_2, 0);
x_7 = lean_ctor_get(x_2, 1);
lean_inc_ref(x_1);
x_8 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_8, 0, x_1);
lean_ctor_set(x_8, 1, x_6);
lean_ctor_set(x_2, 1, x_3);
lean_ctor_set(x_2, 0, x_8);
{
lean_object* _tmp_1 = x_7;
lean_object* _tmp_2 = x_2;
x_2 = _tmp_1;
x_3 = _tmp_2;
}
goto _start;
}
else
{
lean_object* x_10; lean_object* x_11; lean_object* x_12; lean_object* x_13; 
x_10 = lean_ctor_get(x_2, 0);
x_11 = lean_ctor_get(x_2, 1);
lean_inc(x_11);
lean_inc(x_10);
lean_dec(x_2);
lean_inc_ref(x_1);
x_12 = lean_alloc_ctor(0, 2, 0);
lean_ctor_set(x_12, 0, x_1);
lean_ctor_set(x_12, 1, x_10);
x_13 = lean_alloc_ctor(1, 2, 0);
lean_ctor_set(x_13, 0, x_12);
lean_ctor_set(x_13, 1, x_3);
x_2 = x_11;
x_3 = x_13;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant___private_Init_Data_List_Impl_0__List_flatMapTR_go___at___00PachnerInvariant_findImprovingMove_spec__1(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
if (lean_obj_tag(x_2) == 0)
{
lean_object* x_4; 
lean_dec_ref(x_1);
x_4 = lean_array_to_list(x_3);
return x_4;
}
else
{
lean_object* x_5; lean_object* x_6; lean_object* x_7; lean_object* x_8; lean_object* x_9; lean_object* x_10; 
x_5 = lean_ctor_get(x_2, 0);
lean_inc(x_5);
x_6 = lean_ctor_get(x_2, 1);
lean_inc(x_6);
lean_dec_ref(x_2);
x_7 = lean_ctor_get(x_1, 1);
x_8 = lean_box(0);
lean_inc(x_7);
x_9 = lp_pachner__invariant_List_mapTR_loop___at___00PachnerInvariant_findImprovingMove_spec__0(x_5, x_7, x_8);
x_10 = l_List_foldl___at___00Array_appendList_spec__0___redArg(x_3, x_9);
x_2 = x_6;
x_3 = x_10;
goto _start;
}
}
}
static lean_object* _init_lp_pachner__invariant_PachnerInvariant_findImprovingMove___closed__0() {
_start:
{
lean_object* x_1; lean_object* x_2; 
x_1 = lean_unsigned_to_nat(0u);
x_2 = lean_mk_empty_array_with_capacity(x_1);
return x_2;
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_findImprovingMove(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; lean_object* x_4; lean_object* x_5; lean_object* x_6; lean_object* x_7; 
x_3 = lean_ctor_get(x_1, 1);
lean_inc(x_3);
lean_inc_ref(x_1);
x_4 = lean_alloc_closure((void*)(lp_pachner__invariant_PachnerInvariant_findImprovingMove___lam__0___boxed), 3, 2);
lean_closure_set(x_4, 0, x_1);
lean_closure_set(x_4, 1, x_2);
x_5 = lp_pachner__invariant_PachnerInvariant_findImprovingMove___closed__0;
x_6 = lp_pachner__invariant___private_Init_Data_List_Impl_0__List_flatMapTR_go___at___00PachnerInvariant_findImprovingMove_spec__1(x_1, x_3, x_5);
x_7 = l_List_findSome_x3f___redArg(x_4, x_6);
return x_7;
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_greedyImprove(lean_object* x_1, lean_object* x_2, lean_object* x_3) {
_start:
{
lean_object* x_4; uint8_t x_5; 
x_4 = lean_unsigned_to_nat(0u);
x_5 = lean_nat_dec_eq(x_3, x_4);
if (x_5 == 1)
{
lean_dec(x_3);
lean_dec(x_2);
return x_1;
}
else
{
lean_object* x_6; 
lean_inc(x_2);
lean_inc_ref(x_1);
x_6 = lp_pachner__invariant_PachnerInvariant_findImprovingMove(x_1, x_2);
if (lean_obj_tag(x_6) == 0)
{
lean_dec(x_3);
lean_dec(x_2);
return x_1;
}
else
{
lean_object* x_7; lean_object* x_8; lean_object* x_9; lean_object* x_10; lean_object* x_11; lean_object* x_12; lean_object* x_13; lean_object* x_14; lean_object* x_15; lean_object* x_16; lean_object* x_17; lean_object* x_18; 
x_7 = lean_ctor_get(x_6, 0);
lean_inc(x_7);
lean_dec_ref(x_6);
x_8 = lean_ctor_get(x_7, 1);
lean_inc(x_8);
x_9 = lean_ctor_get(x_8, 1);
lean_inc(x_9);
x_10 = lean_ctor_get(x_9, 1);
lean_inc(x_10);
x_11 = lean_ctor_get(x_7, 0);
lean_inc(x_11);
lean_dec(x_7);
x_12 = lean_ctor_get(x_8, 0);
lean_inc(x_12);
lean_dec(x_8);
x_13 = lean_ctor_get(x_9, 0);
lean_inc(x_13);
lean_dec(x_9);
x_14 = lean_ctor_get(x_10, 0);
lean_inc(x_14);
x_15 = lean_ctor_get(x_10, 1);
lean_inc(x_15);
lean_dec(x_10);
x_16 = lean_unsigned_to_nat(1u);
x_17 = lean_nat_sub(x_3, x_16);
lean_dec(x_3);
x_18 = lp_pachner__invariant_PachnerInvariant_pachner23(x_1, x_11, x_12, x_13, x_14, x_15);
x_1 = x_18;
x_3 = x_17;
goto _start;
}
}
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_List_countP_go___at___00PachnerInvariant_countImprovingMoves_spec__0(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
if (lean_obj_tag(x_3) == 0)
{
lean_dec_ref(x_1);
return x_4;
}
else
{
lean_object* x_5; lean_object* x_6; lean_object* x_7; lean_object* x_8; lean_object* x_9; 
x_5 = lean_ctor_get(x_3, 0);
lean_inc(x_5);
x_6 = lean_ctor_get(x_3, 1);
lean_inc(x_6);
lean_dec_ref(x_3);
x_7 = lean_ctor_get(x_5, 0);
lean_inc(x_7);
x_8 = lean_ctor_get(x_5, 1);
lean_inc(x_8);
lean_dec(x_5);
x_9 = lp_pachner__invariant_PachnerInvariant_tetPairToMove(x_7, x_8);
if (lean_obj_tag(x_9) == 0)
{
x_3 = x_6;
goto _start;
}
else
{
lean_object* x_11; lean_object* x_12; lean_object* x_13; lean_object* x_14; lean_object* x_15; lean_object* x_16; lean_object* x_17; lean_object* x_18; lean_object* x_19; uint8_t x_20; 
x_11 = lean_ctor_get(x_9, 0);
lean_inc(x_11);
lean_dec_ref(x_9);
x_12 = lean_ctor_get(x_11, 1);
lean_inc(x_12);
x_13 = lean_ctor_get(x_12, 1);
lean_inc(x_13);
x_14 = lean_ctor_get(x_13, 1);
lean_inc(x_14);
x_15 = lean_ctor_get(x_11, 0);
lean_inc(x_15);
lean_dec(x_11);
x_16 = lean_ctor_get(x_12, 0);
lean_inc(x_16);
lean_dec(x_12);
x_17 = lean_ctor_get(x_13, 0);
lean_inc(x_17);
lean_dec(x_13);
x_18 = lean_ctor_get(x_14, 0);
lean_inc(x_18);
x_19 = lean_ctor_get(x_14, 1);
lean_inc(x_19);
lean_dec(x_14);
lean_inc_ref(x_1);
x_20 = lp_pachner__invariant_PachnerInvariant_isImproving(x_1, x_15, x_16, x_17, x_18, x_19, x_2);
if (x_20 == 0)
{
x_3 = x_6;
goto _start;
}
else
{
lean_object* x_22; lean_object* x_23; 
x_22 = lean_unsigned_to_nat(1u);
x_23 = lean_nat_add(x_4, x_22);
lean_dec(x_4);
x_3 = x_6;
x_4 = x_23;
goto _start;
}
}
}
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_List_countP_go___at___00PachnerInvariant_countImprovingMoves_spec__0___boxed(lean_object* x_1, lean_object* x_2, lean_object* x_3, lean_object* x_4) {
_start:
{
lean_object* x_5; 
x_5 = lp_pachner__invariant_List_countP_go___at___00PachnerInvariant_countImprovingMoves_spec__0(x_1, x_2, x_3, x_4);
lean_dec(x_2);
return x_5;
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_countImprovingMoves(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; lean_object* x_4; lean_object* x_5; lean_object* x_6; lean_object* x_7; 
x_3 = lean_ctor_get(x_1, 1);
x_4 = lean_unsigned_to_nat(0u);
x_5 = lp_pachner__invariant_PachnerInvariant_findImprovingMove___closed__0;
lean_inc(x_3);
lean_inc_ref(x_1);
x_6 = lp_pachner__invariant___private_Init_Data_List_Impl_0__List_flatMapTR_go___at___00PachnerInvariant_findImprovingMove_spec__1(x_1, x_3, x_5);
x_7 = lp_pachner__invariant_List_countP_go___at___00PachnerInvariant_countImprovingMoves_spec__0(x_1, x_2, x_6, x_4);
return x_7;
}
}
LEAN_EXPORT lean_object* lp_pachner__invariant_PachnerInvariant_countImprovingMoves___boxed(lean_object* x_1, lean_object* x_2) {
_start:
{
lean_object* x_3; 
x_3 = lp_pachner__invariant_PachnerInvariant_countImprovingMoves(x_1, x_2);
lean_dec(x_2);
return x_3;
}
}
lean_object* initialize_Init(uint8_t builtin);
lean_object* initialize_pachner__invariant_PachnerInvariant_descent__property(uint8_t builtin);
static bool _G_initialized = false;
LEAN_EXPORT lean_object* initialize_pachner__invariant_PachnerInvariant_lambda__optimization(uint8_t builtin) {
lean_object * res;
if (_G_initialized) return lean_io_result_mk_ok(lean_box(0));
_G_initialized = true;
res = initialize_Init(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
res = initialize_pachner__invariant_PachnerInvariant_descent__property(builtin);
if (lean_io_result_is_error(res)) return res;
lean_dec_ref(res);
lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__0 = _init_lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__0();
lean_mark_persistent(lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__0);
lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__1 = _init_lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__1();
lean_mark_persistent(lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__1);
lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__2 = _init_lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__2();
lean_mark_persistent(lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__2);
lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__3 = _init_lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__3();
lean_mark_persistent(lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__3);
lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__4 = _init_lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__4();
lean_mark_persistent(lp_pachner__invariant_PachnerInvariant_optimize__lam___closed__4);
lp_pachner__invariant_PachnerInvariant_findImprovingMove___closed__0 = _init_lp_pachner__invariant_PachnerInvariant_findImprovingMove___closed__0();
lean_mark_persistent(lp_pachner__invariant_PachnerInvariant_findImprovingMove___closed__0);
return lean_io_result_mk_ok(lean_box(0));
}
#ifdef __cplusplus
}
#endif
