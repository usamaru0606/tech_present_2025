export interface RecordMeal{
    userId:string,
    recordDate:string,
    mealTiming:string,
    stapleFood: string|null,
    mainDish: string|null,
    sideDish: string|null,
    soup: string|null,
    other: string|null,
    totalCalories: number|null,
}